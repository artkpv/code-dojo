# %%
import plotly.express as px

fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
print(fig)
fig.show()
# %%

fig = px.line(
    x=["a","b","c"], y=[1,3,2], # replace with your own data source
    title="sample figure", height=325
)
fig.layout.title.text = "Some other title"
fig.show()
# %%
import plotly.express as px
fig = px.bar(x=list(range(4)), y = [1,2,3,4])
fig.update_xaxes(type='category')
fig.show()

# %%
