class Gene:
    def __init__(self,weights,fitness):
        self.weights=weights
        self.fitness=fitness
class GA:
    def fitness_score(self,funcs,weights):
        k=0
        for i in range(len(weights)):
            k=k+funcs[i](weights[i],i)
            #print(weights[i],f(weights[i]),k)
            i+=1
        return k
    def __init__(self,pop_size,param_range,no_param,funcs):
        from numpy import random
        from numpy import reshape
        self.population=[]
        self.param_range=param_range
        self.Gen_count=0
        self.funcs=funcs
        for i in range(pop_size):
            weights=param_range[0]+(param_range[1]-param_range[0])*random.random(no_param)
            self.population.append(Gene(weights,self.fitness_score(funcs,weights)))
    def sortFitness(self,G1):
        return G1.fitness
    def Gene_Mate(self,G1,G2):
        new_gene_weights=[]
        from numpy import random
        for i in range(len(G1.weights)):
            random_val=random.randint(0,101)
            if random_val<45:#45 % from parent 1
                new_gene_weights.append(G1.weights[i])
            elif random_val<=90:#45 % from parent 2
                new_gene_weights.append(G2.weights[i])
            else:# to maintain diversity add random weight
                new_gene_weights.append(self.param_range[0]+(self.param_range[1]-self.param_range[0])*random.random())
        return Gene(new_gene_weights,self.fitness_score(self.funcs,new_gene_weights))
    def selection(self,num_parent):
        #selecting best num_parent form present populationW
        from numpy import random
        new_population=[]
        n=len(self.population)
        self.population.sort(key=self.sortFitness)
        print('Generation {}'.format(self.Gen_count),'Best Fitness:',self.population[0].fitness)
        for x in self.population[:num_parent]:
            new_population.append(x)
        # mating randomly choosen best 50% population
        for i in range(num_parent,n):
            random_val=random.randint(0,n/2)
            G1=self.population[random_val]
            random_val=random.randint(0,n/2)
            G2=self.population[random_val]
            new_population.append(self.Gene_Mate(G1,G2))
        self.population=new_population
        self.Gen_count+=1
functions=[]
count=0
for i in range(4):
    functions.append(lambda x,count:(-count+x*x))
    count+=1
i=0
for i in range(4):
    print(i,"f({})".format(i)," =",functions[i](i,i))
G=GA(100,(-10,10),4,functions)
Generatons=100
for i in range(Generatons):
    G.selection(15)


