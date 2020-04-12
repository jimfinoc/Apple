#!/usr/bin/env python

import pygame
pygame.init()
# screen = pygame.display.set_mode([1000, 1000])
# screen = pygame.display.set_mode((2**11, 2**10), pygame.FULLSCREEN, pygame.RESIZABLE)
# screen = pygame.display.set_mode((2**11, 2**10), pygame.RESIZABLE)
screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
pygame.display.set_caption("Spaceship Server")
running = True
counter = 0
step = 10
circleCoordinates = [(250,250)]
adjustmentCoordinates = (0,0)
while running:
    if counter > 2:
        counter = 0
        circleCoordinates.append((0,0))
        print len(circleCoordinates)
    counter += 1
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        print adjustmentCoordinates
        if keys[pygame.K_LEFT]:
                adjustmentCoordinates = (-step,0)
        elif keys[pygame.K_RIGHT]:
            adjustmentCoordinates = (step,0)
        elif keys[pygame.K_UP]:
            adjustmentCoordinates = (0,-step)
        elif keys[pygame.K_DOWN]:
            adjustmentCoordinates = (0,step)
        if keys[pygame.K_q]:
            running = False
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    for each in range(len(circleCoordinates)-1,0,-1):
        circleCoordinates[each] = circleCoordinates[each-1]
        circleCoordinates[each] = circleCoordinates[each-1]
    circleCoordinates[0] = (circleCoordinates[0][0]+adjustmentCoordinates[0],circleCoordinates[0][1]+adjustmentCoordinates[1])
    # circleX += x
    # circleY += y
    for each in circleCoordinates:
        pygame.draw.circle(screen, (0, 0, 255), each, 10)
    pygame.draw.circle(screen, (255,255,255), circleCoordinates[0], 7)

    pygame.display.flip()
pygame.quit()


# import tcp_server
# import udp_server

# import socket
# TCP_IP = '127.0.0.1'
# TCP_PORT = 5005
# BUFFER_SIZE = 20  # Normally 1024, but we want fast response
# # BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((TCP_IP, TCP_PORT))
# s.listen(1)
#
# while 1:
#     conn, addr = s.accept()
#     print 'Connection address:', addr
#     while 1:
#         data = conn.recv(BUFFER_SIZE)
#         if not data: break
#         print "received data:", data
#         conn.send("Yes " + data)  # echo
#     # conn.close()
