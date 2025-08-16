def process_forecast_data(forecast_data):
    """Process raw forecast data into daily summaries."""
    daily_forecasts = []
    current_day = None
    day_temps = []
    
    for hour in forecast_data:
        timestamp = datetime.datetime.fromisoformat(hour['timestamp'])
        day = timestamp.date()
        
        if current_day is None:
            current_day = day
            
        if day != current_day:
            if day_temps:
                daily_forecasts.append({
                    'date': current_day,
                    'max': round(max(day_temps)),
                    'min': round(min(day_temps)),
                    'condition': get_most_common_condition(day_conditions)
                })
            current_day = day
            day_temps = []
            day_conditions = []
            
        temp = hour.get('temperature', 0)
        day_temps.append(temp)
        day_conditions.append(hour.get('description', 'clear sky'))
        
    # Add the last day
    if day_temps:
        daily_forecasts.append({
            'date': current_day,
            'max': round(max(day_temps)),
            'min': round(min(day_temps)),
            'condition': get_most_common_condition(day_conditions)
        })
        
    return daily_forecasts

def get_most_common_condition(conditions):
    """Get the most common weather condition from a list."""
    if not conditions:
        return 'clear sky'
    return max(set(conditions), key=conditions.count) 