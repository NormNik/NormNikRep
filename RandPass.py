from asyncio.windows_events import NULL
import random
leitghtP = NULL
Randsim = "zxcvbnmqwertyuiopasdfghjkl[];'./,123456789!@#$%^&*()"
pasw = ""
leitghtP = int(input ("насколько длинный пароль создать"))
for i in range(leitghtP):
    pasw = pasw + str(random.choice(Randsim))
print(pasw)
