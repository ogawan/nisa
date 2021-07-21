from matplotlib import pyplot as plt

def nisa_projection(years=30, annual_deposit=80, initial_budget=100):
  """
  This is a function to plot deposit of TSUMITATE NISA

  Parameters:
  ---------------
    years: integer
      How many years are you going to continue?
    annual_depoist: integer
      Annual deposit into the NISA account. 
    initial_budget: integer
      The initial budget.

  Returns:
  --------------
    pyplot figures. 
  
  """

  for j in [1.00,1.01, 1.02, 1.03, 1.04, 1.05]:
    
    original = initial_budget
    ganbon = []
    box = []

    for i in range(0,years):
      if i == 0:
        box.append(original)
        ganbon.append(original)

      gan = ganbon[-1] + annual_deposit
      original = original * j + annual_deposit
      
      if i > 0:
        box.append(original)
        ganbon.append(gan)
    
    plt.scatter(list(range(0,years)), box)
    plt.legend(["0%", "1%", "2%", "3%", "4%", "5%"])
    plt.xlabel("Years")
    plt.ylabel("Money (Man yen)")

nisa_projection(30, 80, 100)
