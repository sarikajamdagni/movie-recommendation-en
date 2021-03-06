import dash_html_components as html
import dash_core_components as dcc

COLORS = {
    'background': 'white',
    'background1': 'light blue',
    'text': 'black',
}


def layout():
    return html.Div(style={'background-image': 'url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4pHTAKoVkcRe_P-Hfm_BIUppvWlMuO3QAQA&usqp=CAU)' },
                      children=[
                          html.H1(
                              children='Movie Recommendation\n',
                              style={
                                  'textAlign': 'center',
                                  'color': COLORS['text']
                              }
                          ),
                          html.H2(
                                     children='Get your next watch here!!!',
                                      style={
                                       'textAlign': 'center',
                                       'text-font': 'times new roman',
                                       'color': COLORS['text']
                              }
                          ),
                          html.Div(
                              children='Get your next watch just by entering '
                                       'either your favorite movie or your preferred genre '
                                       'or any time period. Tell us your choice & we will find '
                                       'the relevant movies and tv series '
                                       'that will absolutely delight you! So, lets go!!!\n \n',
                              style={
                                  'textAlign': 'center',
                                  'font-style': 'italic',
                                  'color': COLORS['text']
                              }
                          ),
                          html.Div(children=' * \n'
                                            ''
                                            ''
                                            ''
                                   ),
                          dcc.Tabs(id="tabs-example", value='tab-1',
                                   children=[
                                       #dcc.Tab(label='Choice Based Recommendation',
                                        #       value='tab-1'),
                                       dcc.Tab(label='Filter Based Recommendation',
                                               value='tab-1'),
                                   ]),
                          html.Div(id='tabs-content-display')
                      ])