import random
from random import randint
import pygame
import pygame_widgets
from pygame_widgets.button import Button
import time

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption(" магазин 7eleven ")


def newclient():
    c = Client()
    c.genlist()
    guy.update(175, 480)
    all_sprites.draw(screen)
    pygame_widgets.update(events)
    pygame.display.update()
    pygame.display.flip()
    time.sleep(1)
    screen.blit(wht, (480, 175))
    c.buystuff()


class Store:
    def __init__(self, name):
        self.name = name
        self.polka = []
        self.kassalist = []
        self.clientleave = []
        self.clientstay = []

    def getname(self):
        return self.name

    def makeadeal(self, korzina, ex):
        kassa = random.choice(seveneleven.kassalist)

        if kassa.number == 1:
            guy.update(200, 75)
            all_sprites.draw(screen)
            pygame_widgets.update(events)
            pygame.display.update()
            pygame.display.flip()

        elif kassa.number == 2:
            guy.update(200, 700)
            all_sprites.draw(screen)
            pygame_widgets.update(events)
            pygame.display.update()
            pygame.display.flip()

        if len(kassa.ocheredj) < 4:
            kassa.ocheredj.append(self)
            time.sleep(3)
            kassa.extrastuff = kassa.extrastuff + ex
            for i in korzina:
                kassa.money = kassa.money + i.getPrice()
            kassa.ocheredj.remove(self)
            guy.kill()
        else:
            self.makeadeal(korzina, ex)
        return kassa


class Kassa:
    def __init__(self, number):
        self.ocheredj = []
        self.number = number
        self.money = 0
        self.extrastuff = 0

    def getNumber(self):
        return self.number

    def getOchered(self):
        return self.ocheredj

    def getMoney(self):
        return self.money

    def getExtra(self):
        return self.extrastuff


class Tovar:
    def __init__(self, name, price, count, allure):
        self.__price = price
        self.__count = count
        self.__name = name
        if allure == "high":
            self.__allure = 70
        else:
            self.__allure = 25

    def getAll(self):
        return self.__name, self.__price, self.__count

    def getPrice(self):
        return self.__price

    def getName(self):
        return self.__name

    def getCount(self):
        return self.__count

    def changeCount(self, i):
        self.__count = i

    def getAllure(self):
        return self.__allure


class Client:
    def __init__(self):
        self.__list = None

    def genlist(self):
        self.__list = []
        lenlist = randint(1, 5)
        while lenlist > 0:
            self.__list.append(random.choice(seveneleven.polka))
            lenlist = lenlist - 1

    def buystuff(self):
        korzina = []
        extrakorzina = []
        ex = 0
        for tovar in self.__list:

            tov = seveneleven.polka.index(tovar)

            if tov < len(seveneleven.polka) - 1:
                prav = seveneleven.polka[tov + 1]
                if randint(1, 100) <= prav.getAllure():
                    korzina.append(prav)
                    extrakorzina.append(prav)
                    ex = ex + 1

            if tov > 0:
                lev = seveneleven.polka[tov - 1]
                if randint(1, 100) <= lev.getAllure():
                    korzina.append(lev)
                    extrakorzina.append(lev)
                    ex = ex + 1

            for i in seveneleven.polka:
                if tovar.getName() == i.getName() and i.getCount() > 0:
                    i.changeCount(i.getCount() - 1)
                    korzina.append(tovar)

        if korzina == extrakorzina + self.__list or self.__list + extrakorzina or korzina == self.__list + [] or korzina == [] + self.__list:
            seveneleven.makeadeal(self.__list, ex)
            seveneleven.clientstay.append(self)

        else:

            seveneleven.clientleave.append(self)


class Interface:
    databutton = Button(
        screen,
        450,
        500,
        100,
        50,
        text='Data',
        fontSize=50,
        margin=20,
        inactiveColour=(240, 240, 240),
        hoverColour=(220, 220, 220),
        pressedColour=(180, 180, 180),
        radius=20)

    resume = Button(
        screen,
        630,
        700,
        100,
        50,
        text='Resume',
        fontSize=50,
        margin=20,
        inactiveColour=(240, 240, 240),
        hoverColour=(220, 220, 220),
        pressedColour=(180, 180, 180),
        radius=20)


def restock():
    for i in seveneleven.polka:
        i.__count = 10


seveneleven = Store(" 7eleven ")
hleb = Tovar("хлеб", 5, 10, "low")
moloko = Tovar("молоко", 8, 10, "low")
kolbasa = Tovar("колбаса", 10, 10, "low")
konfety = Tovar("конфеты", 15, 10, "high")
seveneleven.polka.append(hleb)
seveneleven.polka.append(konfety)
seveneleven.polka.append(kolbasa)
seveneleven.polka.append(moloko)
kassa1 = Kassa(1)
kassa2 = Kassa(2)
seveneleven.kassalist.append(kassa1)
seveneleven.kassalist.append(kassa2)

FPS = 60

clock = pygame.time.Clock()

running = True
white = (255, 255, 255)
gray = (240, 240, 240)
black = (0, 0, 0)
font = pygame.font.SysFont('Comic Sans MS', 30)
pricefont = pygame.font.SysFont('Comic Sans MS', 30)

nextday = False
ntime = 0
genTime = 0
isday = 0
day = 0
ct = 0
n = 0


class Guy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "стикмен.webp").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (500, 450)

    def update(self, vb, hb):
        self.rect.y = vb
        self.rect.x = hb


def datakassy():
    textl = []
    n = 0
    for kassa in seveneleven.kassalist:
        text = ""
        n = n + 1
        text = text + "касса " + str(n)
        text = text + "   выручка кассы " + str(kassa.getMoney())
        text = text + " количество ненужных покупок " + str(kassa.getExtra())
        textl.append(text)
    return textl


dannie = open(f"{seveneleven.getname()} Данные .txt", "w+")
all_sprites = pygame.sprite.Group()
wht = pygame.image.load("white.png")
bg = pygame.image.load("bg.png")
bigwhite = pygame.image.load("bigwhite.png")
bfdfgf = 0
dc = 0
datac = 0
datacy = 0

while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            dannie = open("Seven Eleven Данные .txt", "w+")
            dannie.write("ушедшие " + str(len(seveneleven.clientleave)) + "\n")
            dannie.write("купившие " + str(len(seveneleven.clientstay)) + "\n")
            for kassa in seveneleven.kassalist:
                n = n + 1
                dannie.write("касса " + str(n) + "\n")
                dannie.write("выручка кассы " + str(kassa.getMoney()) + "\n")
                dannie.write("количество ненужных покупок " + str(kassa.getExtra()) + "\n")
            dannie.close()
            pygame.quit()
            run = False
            quit()
    datagen = ("ушедшие " + str(len(seveneleven.clientleave)) + "   купившие " + str(len(seveneleven.clientstay)))
    datakass1 = datakassy()[0]
    datakass2 = datakassy()[1]

    datagen_surface = font.render(datagen, False, black)
    datakass1_surface = font.render(datakass1, False, black)
    datakass2_surface = font.render(datakass2, False, black)
    day_surface = font.render(f'День {day + 1}', False, black)
    hleb_surface = font.render(str(hleb.getPrice()), False, black)
    konfety_surface = font.render(str(konfety.getPrice()), False, black)
    kolbasa_surface = font.render(str(kolbasa.getPrice()), False, black)
    moloko_surface = font.render(str(moloko.getPrice()), False, black)

    if Interface.databutton.clicked:
        datac = 1
        Interface.resume.setY(500)

    if Interface.resume.clicked:
        datac = 0
        Interface.resume.setY(700)

    if datac == 1:
        while dc == 0:
            dannie = open(f"{seveneleven.getname()} Данные .txt", "w+")
            dc = 1
        dannie.write(" " + "\n")
        dannie.write("ушедшие " + str(len(seveneleven.clientleave)) + "\n")
        dannie.write("купившие " + str(len(seveneleven.clientstay)) + "\n")
        for kassa in seveneleven.kassalist:
            n = n + 1
            dannie.write("касса " + str(n) + "\n")
            dannie.write("выручка кассы " + str(kassa.getMoney()) + "\n")
            dannie.write("количество ненужных покупок " + str(kassa.getExtra()) + "\n")
        n = 0
        dannie.close()

        screen.blit(bigwhite, (0, 0))
        screen.blit(datagen_surface, (300, 0))
        screen.blit(datakass1_surface, (0, 50))
        screen.blit(datakass2_surface, (0, 100))





    else:

        screen.blit(bg, (0, 0))
        screen.blit(day_surface, (50, 0))
        screen.blit(hleb_surface, (400, 120))
        screen.blit(konfety_surface, (450, 120))
        screen.blit(kolbasa_surface, (520, 120))
        screen.blit(moloko_surface, (590, 120))
        while bfdfgf == 0:
            pygame_widgets.update(events)
            pygame.display.update()
            pygame.display.flip()
            bfdfgf = 1

        if ntime % FPS == 0:
            genTime = int(ntime / FPS)
            isday = 1
            ct = randint(0, 100)
            if ct >= 80:
                print(" новый клиент ")
                guy = Guy()
                all_sprites.add(guy)
                all_sprites.draw(screen)
                pygame_widgets.update(events)
                pygame.display.update()
                pygame.display.flip()
                time.sleep(1)
                screen.blit(wht, (472, 425))
                newclient()

        ntime = ntime + 1

        if genTime % 20 == 0 and genTime != 0 and isday == 1:
            nextday = True
            isday = 0

        if nextday == True:
            day = day + 1
            restock()
            print("товары пополнены")
            nextday = False

    dc = 0
    all_sprites.draw(screen)
    pygame_widgets.update(events)
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
