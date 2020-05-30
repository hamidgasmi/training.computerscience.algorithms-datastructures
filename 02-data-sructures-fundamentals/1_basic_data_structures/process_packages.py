from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    #O(b)
    def process(self, request):

        # Dequeue all finish times before the current request arrive at time
        while len(self.finish_time) != 0 and self.finish_time[0] <= request.arrived_at:
            self.finish_time.pop(0)
        
        if len(self.finish_time) < self.size:
             start_time = request.arrived_at if len(self.finish_time) == 0 else self.finish_time[len(self.finish_time) - 1]
             self.finish_time.append(start_time + request.time_to_process)

        elif len(self.finish_time) == self.size:
            start_time = -1

        return Response(start_time == -1, start_time)

#O(n * b)
def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
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