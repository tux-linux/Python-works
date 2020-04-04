def graphA():
    import seaborn as sns
    import numpy as np

    x = np.arange(5, 14, 3)
    y = np.sin(x)
    y2 = np.cos(x)

    ax1 = sns.lineplot(x, y2)
    sns.lineplot(x = x, y = y, ax=ax1)
    print("I'm A.")

def graphDistorted():
    import seaborn as sns
    import numpy as np

    x = np.arange(1, 8*np.pi, 1)
    y = np.sin(x)
    y2 = np.cos(x)

    ax1 = sns.lineplot(x, y2)
    sns.lineplot(x = x, y = y, ax=ax1)
    
def graphSound1():
    import seaborn as sns
    import numpy as np

    x = np.arange(3, 99*np.pi, 3)
    y = np.sin(x)
    y2 = np.cos(x)

    ax1 = sns.lineplot(x, y2)
    sns.lineplot(x = x, y = y, ax=ax1)
    print("N.B.: It's a drama...")
def graphSound2():
    import seaborn as sns
    import numpy as np

    x = np.arange(3, 49*np.pi, 3)
    y = np.sin(x)
    y2 = np.cos(x)

    ax1 = sns.lineplot(x, y2)
    sns.lineplot(x = x, y = y, ax=ax1)
    print("Good music!")
def graphSunGlasses():
    import seaborn as sns
    import numpy as np

    x = np.arange(3, 40*np.pi, 3)
    y = np.sin(x)
    y2 = np.cos(x)
    y3 = np.cos(y2)

    ax1 = sns.lineplot(x, y3)
    sns.lineplot(x = x, y = y, ax=ax1)
    print("I'm cool.....")
def graphFluid1():
    import seaborn as sns
    import numpy as np

    x = np.arange(3, 10*np.pi, 0.01)
    y = np.sin(x)
    y2 = np.cos(x)

    ax1 = sns.lineplot(x, y2)
    sns.lineplot(x = x, y = y, ax=ax1)
    print("Do you like the smooth curves?")
    
def graphX():
    import seaborn as sns
    import numpy as np

    x = np.arange(0.01, 0.50*np.pi, 0.01)
    y = np.sin(x)
    y2 = np.cos(x)

    ax1 = sns.lineplot(x, y2)
    sns.lineplot(x = x, y = y, ax=ax1)
    print("It makes me thinking at Xbox... And you?")
def graphFluid2():
    import seaborn as sns
    import numpy as np

    x = np.arange(3, 4*np.pi, 0.01)
    y = np.sin(x)
    y2 = np.cos(x)

    ax1 = sns.lineplot(x, y2)
    sns.lineplot(x = x, y = y, ax=ax1)
    print("Fluid. Smooth. Beautiful.")

print("Seaborn Graphs Demo - Please choose a model of graph below")
print("1. Fluid\n2. Fluid-1\n3. X\n4. Distorsion\n5. A\n6. Sunglasses\n7. Sound-1\n8. Sound-2\n\nPlease pick a number")
graph = input("")
if graph == "1":
    graphFluid2()
elif graph == "2":
    graphFluid1()
elif graph == "3":
    graphX()
elif graph == "4":
    graphDistorted()
elif graph == "5":
    graphA()
elif graph == "6":
    graphSunGlasses()
elif graph == "7":
    graphSound1()
elif graph == "8":
    graphSound2()