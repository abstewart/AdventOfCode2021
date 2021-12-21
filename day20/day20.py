def printImage(image):
    for i in image:
        print(i)
    return

#convert image to a list of lists
def convert(image):
    for i, a in enumerate(image):
        image[i] = [char for char in a]
    return

def expand(image, num, ch):

    #add num "." to the beginning and end of each existing line
    for i in range(len(image)):
        image[i] = ch * num + image[i] + ch * num
    #add the beginning and end rows of '.'
    for j in range(num):
        image.insert(0, ch * len(image[0]))
        image.append(ch * len(image[0]))

#image is the image to expand/convert
#num is the number of times to expand it
#each expansion adds a ring of '.' around the edges
#ch is the character to expand with
def expandAndConvert(image, num, ch):
    #first expand
    expand(image, num, '.')
    #then convert
    convert(image)
    return

def convertToBin(string):
    ans = ''
    for a in string:
        if a == '.':
            ans += '0'
        elif a == '#':
            ans += '1'
    return ans
#arr is the image to enhance
#lookup is the string to lookup the conversion
#dots is True if the infinite plane is dots or dashes
def enhance(arr, lookup, dots):
    ans = [dots] * len(arr)
    for i in range (len(ans)):
        ans[i] = [dots]*len(arr[0])
    if dots:
        blank = '.'
    else:
        blank = '#'
    #loop through the image
    for x, a in enumerate(image):
        for y, b in enumerate(a):
            binary = ''
            #top of the arr
            if x == 0:
                binary = blank * 3
                #left side of the arr
                if y == 0:
                    binary += blank
                    binary += arr[x][y]
                    binary += arr[x][y+1]
                    binary += blank
                    binary += arr[x+1][y]  
                    binary += arr[x+1][y+1]
                #right side of the arr
                elif y == len(a)-1:
                    binary += arr[x][y-1]
                    binary += arr[x][y]
                    binary += blank
                    binary += arr[x+1][y-1]
                    binary += arr[x+1][y]
                    binary += blank
                #middle of the arr
                else:
                    binary += arr[x][y-1]
                    binary += arr[x][y]
                    binary += arr[x][y+1]
                    binary += arr[x+1][y-1]
                    binary += arr[x+1][y]
                    binary += arr[x+1][y+1]
            #bottom of the arr
            elif x == len(image)-1:
                #left side of the arr
                if y == 0:
                    binary += blank
                    binary += arr[x-1][y]
                    binary += arr[x-1][y+1]
                    binary += blank
                    binary += arr[x][y]
                    binary += arr[x][y+1]
                    binary += blank * 3
                    
                #right side of the arr
                elif y == len(a)-1:
                    binary += arr[x-1][y-1]
                    binary += arr[x-1][y]
                    binary += blank
                    binary += arr[x][y-1]
                    binary += arr[x][y]
                    binary += blank
                    binary += blank * 3
                    
                #middle of the arr
                else:
                    binary += arr[x-1][y-1]
                    binary += arr[x-1][y]
                    binary += arr[x-1][y+1]
                    binary += arr[x][y-1]
                    binary += arr[x][y]
                    binary += arr[x][y+1]
                    binary += blank * 3
            #middle of the arr
            else:
                #lef side of the arr
                if y == 0:
                    binary += blank
                    binary += arr[x-1][y]
                    binary += arr[x-1][y+1]
                    binary += blank
                    binary += arr[x][y]
                    binary += arr[x][y+1]
                    binary += blank
                    binary += arr[x+1][y]
                    binary += arr[x+1][y+1]
                #right side of the arr
                elif y == len(a)-1:
                    binary += arr[x-1][y-1]
                    binary += arr[x-1][y]
                    binary += blank
                    binary += arr[x][y-1]
                    binary += arr[x][y]
                    binary += blank
                    binary += arr[x+1][y-1]
                    binary += arr[x+1][y]
                    binary += blank
                #true middle of the arr
                else:
                    binary += arr[x-1][y-1]
                    binary += arr[x-1][y]  
                    binary += arr[x-1][y+1]
                    binary += arr[x][y-1]  
                    binary += arr[x][y]
                    binary += arr[x][y+1]  
                    binary += arr[x+1][y-1]
                    binary += arr[x+1][y]  
                    binary += arr[x+1][y+1]
            #have the binary string now
            #print('str: ', binary)
            binary = convertToBin(binary)
            #print('bin: ', binary)
            ans[x][y] = lookup[int(binary, 2):int(binary, 2) + 1]
                    
    return ans

def countHashes(arr):
    cnt = 0
    for a in arr:
        for b in a:
            if b == '#':
                cnt += 1
    return cnt

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    lines = fd.read().splitlines()
    fd.close

    lookup = lines[0]
    image = lines[2:]

    print(lookup)
    print(image)

    #expand the image to add 2 entries of dots around everything
    
    #printImage(image)
    expandAndConvert(image, 50, ',')
    #printImage(image)
    #image = enhance(image, lookup, True)
    #print('enhanced image')
    #printImage(image)
    #image = enhance(image, lookup, False)
    #print('2x enhanced image')
    #printImage(image)
    #print('number of #: ', countHashes(image))

    #part2
    for i in range(50):
        if i % 2 == 0:
            image = enhance(image, lookup, True)
        else:
            image = enhance(image, lookup, False)
    print('number of #: ', countHashes(image))
                
    
    
