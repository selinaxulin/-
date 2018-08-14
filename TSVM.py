# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:30:16 2018

@author: Selina
"""

import numpy as np
class particle:
    def __init__(self):
        self.pos=0  #粒子当前位置
        self.speed=0
        self.pbest=0
        
class PSO:
    def __init__(self):
        self.w=0.5
        self.c1=1
        self.c2=1
        self.gbest=0
        self.N=20
        self.POP=[]
        self.iter_N=100
    def fitness(self,x):
        return x+10*np.sin(5*x)+7*np.cos(4*x)
    def g_best(self,pop):
        for bird in pop:
            if bird.fitness > self.fitness(self.gbest):
                self.gbest=bird.pos
    #初始化种群
    
    def initPopulation(self,pop,N):
        for i in range(N):
            bird=particle()
            bird.fitness=self.fitness(bird.pos)
            bird.pbest=bird.fitness
            pop.append(bird)
            #找到种群的最有位置
            self.g_best(pop)
            #更新速度和位置
    def update(self,pop):
        for bird in pop:
            #速度更新
            speed=self.w*bird.speed+self.c1*np.random.random()*(bird.pbest-bird.pos)+self.c2*np.random.random()*(
                    self.gbest-bird.pos)
            #位置更新
            pos=bird.pos+speed
            if -10 < pos <10:
                bird.pos=pos
                bird.speed=speed
                bird.fitness=self.fitness(bird.pos)
                
                if bird.fitness > self.fitness(bird.pbest):
                    bird.pbest=bird.pos
        
    def implement(self):
        self.initPopulation(self.POP,self.N)
            
        for i in range(self.iter_N):
            self.update(self.POP)
            self.g_best(self.POP)
pso=PSO()
pso.implement()
for ind in pso.POP:
    print('x=',ind.pos,'f(x)=',ind.fitness)
import matplotlib.pyplot as plt
def func(x):
    return x+10*np.sin(5*x)+7*np.cos(4*x)
x=np.linspace(-10,10,10000)
y=func(x)
scatter_x=np.array([ind.pos for ind in pso.POP])
scatter_y=np.array([ind.fitness for ind in pso.POP])
plt.plot(x,y)
plt.scatter(scatter_x,scatter_y,c='r')
plt.show()