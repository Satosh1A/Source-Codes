import serial
import time

arduino = serial.Serial('COM5',115200)
situation = 1

time.sleep(1)

def send_steps(microstep_mode,steps):
    a = str(microstep_mode)+" "+str(steps)
    arduino.write(bytes(a,'ascii'))

while True:
    microstep_mode = input("マイクロステップモードを選択してください．\n1: フルステップ\n2: ハーフステップ\n4: 1/4ステップ\n8: 1/8ステップ\n16: 1/16ステップ\n")
    if microstep_mode not in ['1', '2', '4', '8', '16']:
        continue
    while situation == 1:
        steps = input("動かしたい長さを入力してください(単位:μm)\n終了する場合は'e'を入力\nステップモードの変更は'm'を入力\n")
        
        if steps == 'e':
            situation = 0
            break
        elif steps == 'm':
            break
        if steps.isdigit() or (steps.startswith('-') and steps[1:].isdigit()):
            steps=int(int(steps)*int(microstep_mode)/25)
            send_steps(microstep_mode,steps)
            
    if situation == 0:
        break
    
    

arduino.close()