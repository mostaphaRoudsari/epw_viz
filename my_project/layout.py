import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from .server import app 

def build_footer():
    """ Build the footer at the bottom of the page
    """
    return html.Div(
        id = "footer-container",
        className = "container-row",
        children = [
            html.A(
                children = [
                    html.Img(
                        id = "cbe-logo", 
                        src = "assets/img/cbe-logo.png"
                    )
                ],
                href = 'https://cbe.berkeley.edu/'
            ),
            html.Div(
                className = "container-col",
                children = [
                    html.P("Contact"),
                    html.P("Filler text"),
                ]
            ),
            html.Div(
                className = "container-col",
                children = [
                    html.P("Filler text"),
                    html.P("Filler text")
                ]
            ),
        ]
    )

def build_banner():
    """ Build the banner at the top of the page.

    TO DO: add in global and local buttons 
    """
    return html.Div(
        id = "banner",
        className = "container-row",
        children = [
            html.Div(
                id = "banner-text-left",
                className = "container-col",
                children = [
                    html.H1(
                        id = "banner-title",
                        children = ["EPW Viz Tool"]),
                    html.H5(
                        id = "banner-subtitle",
                        children = ["Current Location: N/A"]),
                ]
            ),
            html.Div(
                id = "banner-text-right",
                className = "container-col",
                children = [
                    dbc.RadioItems(
                        options = [
                            {"label": "Global Value Ranges", "value": "global"},
                            {"label": "Local Value Ranges", "value": "local"},
                        ],
                        value = "global",
                        id = "global-local-radio-input",
                        inline = True
                    ),
                ]
            )
        ]
    )

def build_tabs():
    """ Build the seven different tabs. 
    """
    return html.Div(
        id = "tabs-container",
        children = [
            dcc.Tabs(
                id = 'tabs', 
                parent_className = 'custom-tabs',
                value = 'tab-1', 
                children = [
                    dcc.Tab(
                        label = 'Select Weather File', 
                        value = 'tab-1',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected'),
                    dcc.Tab(
                        label = 'Climate Summary', 
                        value = 'tab-2',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected'),
                    dcc.Tab(
                        label = 'Temperature/Humidity', 
                        value = 'tab-3',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected'),
                    dcc.Tab(
                        label = 'Sun and Rain', 
                        value = 'tab-4',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected'),
                    dcc.Tab(
                        label = 'Wind', 
                        value = 'tab-5',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected'),
                    dcc.Tab(
                        label = 'Query Data', 
                        value = 'tab-6',
                        className='custom-tab',
                        selected_className='custom-tab--selected'),
                    dcc.Tab(
                        label = 'Outdoor Comfort', 
                        value = 'tab-7',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected'),
                    dcc.Tab(
                        label = 'Natural Ventilation', 
                        value = 'tab-8',
                        className = 'custom-tab',
                        selected_className = 'custom-tab--selected'),
                ]
            ),
            html.Div(
                id = 'store-container', 
                children = [
                    store(),
                    html.Div(
                        id = 'tabs-content'
                    ), 
                    build_footer(), 
                ]
            ),
            
        ]
    )

def store():
    return html.Div(
        id = "store",
        children = [
            dcc.Store(id = 'df-store', storage_type = 'session'),
            dcc.Store(id = 'meta-store', storage_type = 'session'),
        ])