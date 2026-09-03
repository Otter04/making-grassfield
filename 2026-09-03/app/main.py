import os
import platform

learner_name = os.getenv("LEARNER_NAME", "Docker learner")

print(f"Hello, {learner_name}!")
print("This Python process is running inside a container.")
print(f"Architecture: {platform.machine()}")
print("The image provided the files and startup command.")
print("The container provided the running environment.")

#뭐하는 코드들일까?
