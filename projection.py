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

# Reference: https://plotly.com/python/figure-labels/
import pandas as pd
import plotly.graph_objects as go

def nisa_projection_plotly(years=30, annual_deposit=80, initial_budget=100):
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

  dic_ = {}
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

    dic_["{} %".format(str(j)[-1])] = box

  df = pd.DataFrame(dic_)

  fig = go.Figure()
  for i in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[i],name=i))

  fig.update_layout(
    title="NISA PLOT",
    xaxis_title="Years",
    yaxis_title="Man Yen",
    width=500,
    height=400,
    )

  fig.show()
  
nisa_projection(30, 80, 100)
nisa_projection_plotly(30, 80, 100)
