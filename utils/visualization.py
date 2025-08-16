"""
Visualization utilities for climate data.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from .chatbot import ChatBot

def plot_climate_data(district: str) -> go.Figure:
    """
    Create an interactive visualization of climate data for a district.
    
    Args:
        district: Name of the district
        
    Returns:
        Plotly figure with climate data visualization
    """
    # Initialize chatbot to get data
    chatbot = ChatBot()
    
    # Get climate data for the district
    if district.lower() in chatbot.climate_data:
        data = chatbot.climate_data[district.lower()]['climate_profile']
        
        # Extract data points
        temp_data = {
            'Annual Average': float(data['temperature']['annual_average'].replace('°C', '')),
            'Summer Max': float(data['temperature']['summer_max'].replace('°C', '')),
            'Winter Min': float(data['temperature']['winter_min'].replace('°C', ''))
        }
        
        rainfall = float(data['rainfall']['annual_average'].replace('mm', ''))
        humidity = float(data['humidity']['annual_average'].replace('%', ''))
        wind_speed = float(data['wind']['average_speed'].replace('km/h', ''))
        
        # Create figure with subplots
        fig = go.Figure()
        
        # Temperature bar chart
        for param, value in temp_data.items():
            fig.add_trace(go.Bar(
                name=param,
                x=['Temperature'],
                y=[value],
                text=[f'{value}°C'],
                textposition='auto',
            ))
        
        # Add other climate parameters
        fig.add_trace(go.Bar(
            name='Rainfall',
            x=['Rainfall'],
            y=[rainfall],
            text=[f'{rainfall}mm'],
            textposition='auto',
        ))
        
        fig.add_trace(go.Bar(
            name='Humidity',
            x=['Humidity'],
            y=[humidity],
            text=[f'{humidity}%'],
            textposition='auto',
        ))
        
        fig.add_trace(go.Bar(
            name='Wind Speed',
            x=['Wind Speed'],
            y=[wind_speed],
            text=[f'{wind_speed}km/h'],
            textposition='auto',
        ))
        
        # Update layout
        fig.update_layout(
            title=f'Climate Data for {district.title()}',
            barmode='group',
            xaxis_title='Parameters',
            yaxis_title='Values',
            height=500,
            showlegend=True,
            legend_title='Measurements',
            template='plotly_white'
        )
        
        return fig
    else:
        # Return empty figure with error message
        fig = go.Figure()
        fig.add_annotation(
            text=f"No climate data available for {district}",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False
        )
        return fig

def create_climate_heatmap(
    data: Dict[str, float],
    title: str,
    color_scale: Optional[List[str]] = None,
    zmin: Optional[float] = None,
    zmax: Optional[float] = None
) -> go.Figure:
    """
    Create an interactive heat map for climate data across districts.
    
    Args:
        data: Dictionary mapping district names to values
        title: Title for the heat map
        color_scale: Optional custom color scale
        zmin: Optional minimum value for color scale
        zmax: Optional maximum value for color scale
        
    Returns:
        Plotly figure object
    """
    # Default color scale if none provided
    if color_scale is None:
        color_scale = ['#313695', '#4575b4', '#74add1', '#abd9e9', 
                      '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', 
                      '#f46d43', '#d73027', '#a50026']
    
    # Create figure
    fig = go.Figure(data=go.Heatmap(
        z=list(data.values()),
        x=list(data.keys()),
        y=['Value'],
        colorscale=color_scale,
        zmin=zmin,
        zmax=zmax,
        hoverongaps=False,
        showscale=True,
        colorbar=dict(
            title=dict(
                text='Value',
                side='right'
            )
        )
    ))
    
    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title='District',
        yaxis_title='',
        height=400,
        margin=dict(t=50, l=50, r=50, b=50)
    )
    
    return fig

def create_temporal_heatmap(
    data: pd.DataFrame,
    title: str,
    x_label: str = 'Time',
    y_label: str = 'District',
    color_scale: Optional[List[str]] = None
) -> go.Figure:
    """
    Create a temporal heat map showing changes over time.
    
    Args:
        data: DataFrame with time index and district columns
        title: Title for the heat map
        x_label: Label for x-axis
        y_label: Label for y-axis
        color_scale: Optional custom color scale
        
    Returns:
        Plotly figure object
    """
    if color_scale is None:
        color_scale = ['#313695', '#4575b4', '#74add1', '#abd9e9', 
                      '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', 
                      '#f46d43', '#d73027', '#a50026']
    
    fig = go.Figure(data=go.Heatmap(
        z=data.values,
        x=data.index,
        y=data.columns,
        colorscale=color_scale,
        hoverongaps=False,
        showscale=True,
        colorbar=dict(
            title='Value',
            titleside='right'
        )
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=500,
        margin=dict(t=50, l=50, r=50, b=50)
    )
    
    return fig 