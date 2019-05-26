from random import shuffle, randrange
import pygame
from time import sleep
##############################
window = pygame.display.set_mode((1920,1080))
pygame.font.init()
fps = pygame.time.Clock()
myfont = pygame.font.SysFont('Consolas', 100)
pygame.display.set_caption("Hello World")
imgs = []
MAX = 4
for i in range(1,MAX+1):
    imgs.append(pygame.image.load(str(i)+'.png'))

ptsImg = pygame.image.load("ptspts.png")
ttleImg = pygame.image.load("ttlttl.png")
resetImg = pygame.image.load("reset.png")

key = -1
displayNum = []
cnt = 0
tcnt = 0
lst = [i for i in range(1,MAX+1)]
shuffle(lst)
ans = []
##############################

def reset():
    global key,displayNum,cnt,tcnt,lst,ans
    key = -1
    displayNum = []
    cnt = 0
    tcnt = 0
    lst = [i for i in range(1,MAX+1)]
    shuffle(lst)
    ans = []

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[0]>145 and pos[0]<1770 and pos[1]>330 and pos[1]<570:
                    key = 1
                if key == 2 and pos[0]>75 and pos[0]<305 and pos[1]>880 and pos[1]<960:
                    reset()


        window.fill(pygame.Color(255,255,255))

        '''
        for i in range(1,MAX+1):
            window.blit(imgs[i-1],((i-1)*250,40))
        '''

        window.blit(ttleImg,(30,5))
        if key==-1:
            window.blit(ptsImg,(140,300))

        elif key == 1:
            tempdisplayNum = []
            if tcnt == MAX-1:
                cnt = 30

            if cnt < 30 and key != 2:
                tempdisplayNum = displayNum[::]
                tempdisplayNum.append(lst[cnt%(MAX-tcnt)])
                for i in range(tcnt+1):
                    window.blit(imgs[tempdisplayNum[i]-1],((i)*450+80,330))
                
                cnt += 1
                sleep(i*0.01)

            if cnt == 30 and key != 2:
                shuffle(lst)
                cnt = 0
                tcnt += 1
                l = lst.pop()
                displayNum.append(l)
                ans.append(l)

            if tcnt == MAX and key != 2:
                cnt = 31
                for i in range(0,tcnt):
                    window.blit(imgs[ans[i]-1],((i)*450+80,330))
                key = 2

        elif key == 2:
            for i in range(0,MAX):
                window.blit(imgs[ans[i]-1],((i)*450+80,330))
            window.blit(resetImg,(70,870))

        pygame.display.flip()
        fps.tick(30)

except Exception as e:
    print(e,"Thank you for using")
