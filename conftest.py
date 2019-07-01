

def pytest_collectstart(collector):
    args = 'text/html', 'application/javascript', 'stderr', 'text/vnd.plotly.v1+html'
    try:
        collector.skip_compare += args
    except:
        collector.skip_compare = []
        collector.skip_compare += args