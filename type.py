import pyautogui,sys,time
total = 0
word = input('Word: ')
no = int(input('Number of Times: '))
de = int(input('Delay: '))
time.sleep(de)
for i in range(no):
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    total += 1
print('Process Completed...//')
print('No of Messages send: '+ str(total))
sys.exit

