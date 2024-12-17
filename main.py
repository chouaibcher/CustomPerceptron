"""
@ First Name : Chouaib
@ Last Name :  CHERIBET CHERIF
@ 2023-2024
All Right Reserved
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from CustomPerceptron import CustomPerceptron 
from MyFunctions import saveOutput
from Colors import Colors

print(f"########### {Colors.GREEN} CHERIBET CHEIF CHOUAIB {Colors.RESET}############")
def main():
    # load iris data from sklearn
    data=load_iris()
    ##################################################
    ###features X1,X2,X3,X4 because  we have 4 features
    x=data.data
    #print(x[:10])
    print(f"# number of examples: {Colors.RED} {x.shape[0]} {Colors.RESET}")
    print(f"# number of features: {Colors.RED} {x.shape[1]} {Colors.RESET}")
    print(f"# features: {data.feature_names}")
    ##################################################

    ###target - desired output y= 0 or 1 or 2 -

    y=data.target
    #print(y[:150])
    print(f"# classes: {data.target_names}")

    ##################################################


    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=2)

    print(f"----------- {Colors.YELLOW} Y' predicted{Colors.RESET} -------------")
    test=CustomPerceptron()
    test.fit(x,y)

    print(f" fitted weights =  {test.getWeights()}")
    print(f" bias W0= {test.getBias()}")

    Ypredicted=test.predict(x_test[:38])
    print(f"{Colors.YELLOW}{Colors.BOLD}y'={Ypredicted} {Colors.RESET}")
    print('Accuracy:', test.score(x_train, y_train))
    print('Accuracy:', test.score(x_test, y_test))

    """
    print("-----------Sklearn Perceptron Y' -------------")

    clf = Perceptron(tol=5e-8, max_iter=1000, eta0=0.01)
    clf.fit(x_train, y_train)

    print('Accuracy:', clf.score(x_train, y_train))

    print('Accuracy:', clf.score(x_test, y_test))

    print(clf.predict(x_test[:38]))

    print(clf.predict(([[5.6, 3.6]])))
    """    

    print(f"------------{Colors.GREEN} Y desired {Colors.RESET}------------")
    print(f"y={y_test[:38]}")

    ## save output
    weights = test.getWeights()
    function=f"function={weights[0]}*x1+{weights[1]}*x2+{weights[2]}*x3+{weights[3]}*x4+{test.getBias()}\n"
    saveOutput(function,Ypredicted)


if __name__=="__main__":
    main()