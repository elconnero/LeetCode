class Solution(object):
    def exclusiveTime(self, n, logs):
        stack = []
        prev_time = 0
        result = {i: 0 for i in range(n)}

        for log in logs:
            parts = log.split(":")
            function_id = int(parts[0])
            action = parts[1]
            timestamp = int(parts[2])

            if action == "start":
                if stack:  # if a function is already running, give it credit first
                    result[stack[-1]] += timestamp - prev_time
                stack.append(function_id)
                prev_time = timestamp
            else:
                calculate = stack.pop()
                result[calculate] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return list(result.values())