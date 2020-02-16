from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = 0
        self.queue = []

    def full(self):
        return len(self.queue) == self.size

    def empty(self):
        return len(self.queue) == 0

    def enqueue(self, request):
        if self.full():
            return False
        else:
            self.queue.append(request)
            return True

    def process(self):
        
        if not self.empty():
            request = self.queue[0]
            response = Response(False, max(request.arrived_at, self.finish_time))
            self.finish_time = response.started_at + request.time_to_process
            self.queue.pop(0)
            return response

def process_requests(requests, buffer):
    responses = []

    if len(requests) == 0:
        return responses

    # 0. Append to the buffer:
    i = 0
    #curr_time = requests[i].arrived_at
    while not buffer.full() and i < len(requests): #and requests[i].arrived_at == curr_packets_arriving_time:
        buffer.enqueue(requests[i])
        i += 1

    while (not buffer.empty()):

        # 1. Process a Request:
        
        while not buffer.empty() and (i >= len(requests[i]) or buffer.finish_time + buffer.queue[0].time_to_process <= requests[i].arrived_at):
            responses.append(buffer.process())
            
            
        # 2. Drop all requests arrived before the end of current request: response.started_at + Request.time_to_process
        while i < len(requests) and requests[i].arrived_at < buffer.finish_time:
            responses.append(Response(True, -1))
            i += 1

        # 3. Append to the buffer (1 spot available)
        #if i < len(requests): 
            #curr_packets_arriving_time = requests[i].arrived_at
        while not buffer.full() and i < len(requests):
            buffer.enqueue(requests[i])
            i += 1

    return responses

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
