from plotly import tools
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

note_names = ["E", "F", "G", "A", "B", "C", "D"]

def check_keystroke(title_input, melody):
	keystroke = ""
	fill_measures = False
	while keystroke != "Print" and not fill_measures:
		keystroke = raw_input("Enter a note(A, C, F, etc): ")
   		if keystroke in note_names:
   			for i in range(0, len(note_names)):
   				if note_names[i] == keystroke:
   					melody.append(i / 2.0)
   		elif keystroke != "Print":
   			print 'Please either enter a note or enter "Print"'
   		elif keystroke == "Print":
   			if len(melody) % 4 != 0:
   				print """
\nYour melody does not evenly fill your measures.
Please add more notes.\n
"""
				check_keystroke(title_input, melody)
			else:
				fill_measures = True
				make_graph(melody, title_input)

def make_graph(melody, title_input):
    plots = []

    # Make the graph a subplot
    fig = tools.make_subplots(rows=1,
        cols=2,
        shared_xaxes=True,
        shared_yaxes=True
    )

    for note in range(0, len(melody)):
        # Make x-axis length into list
        x_axis_length = []
        for i in range(0, len(melody)):
            x_axis_length.append(i + 0.5)

        # Make graph of melody
        graph_melody = go.Scatter(
            x= x_axis_length,
            y= melody,
            mode='markers',
            marker = dict(
                size = 30,
                color = 'rgba(0, 0, 0, 1)'
            ),
        )

        # Add melody graph to the subplot
        plots.append(graph_melody)

    # Make formatting for graph into list format
    total_measures = int(len(melody) / 4)
    barline_places = []
    height_list = []
    girth = []
    for i in range(0, total_measures):
        barline_places.append(i * 4)
        height_list.append(4)
        girth.append(.05)

    # Make graph of barlines
    barlines = go.Bar(
        x= barline_places,
        y= height_list,
        width = girth
    )

    # Add barlines graph to the subplot
    plots.append(barlines)

    # Set layout for graphs
    layout = go.Layout(
        height=600,
        width=150*len(melody),
        title=title_input,
        showlegend = False,

        xaxis=dict(
            autorange=False,
            range=[0, len(melody)],
            showticklabels=False,
            autotick=False,
            ticks='',
        ),

        yaxis=dict(
            autorange=False,
            range=[-0.5,4.5],
            showticklabels=False,
            dtick=1
        )
    )

    # Plot graphs
    fig = dict(data=plots, layout=layout)
    plotly.offline.plot(fig, filename='notation')

def notate_melody():
	melody = []
	title_input = raw_input("Please enter a title for the piece: ")
	check_keystroke(title_input, melody)

notate_melody()