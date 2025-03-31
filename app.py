"""
Web interface for the nanozyme multi-agent framework.
"""
from flask import Flask, render_template, request
from src.framework import SimpleReActFramework
from src.utils.logger import setup_logger

import os
os.environ['HTTPS_PROXY'] = "http://127.0.0.1:7890"
os.environ['HTTP_PROXY'] = "http://127.0.0.1:7890"

app = Flask(__name__)
logger = setup_logger("nanozyme_framework.web")

def format_result(result_text):
    """Format result text to reduce excessive indentation and improve readability"""
    if not result_text:
        return ""
        
    # Remove excessive spaces and indentation
    lines = result_text.split('\n')
    formatted_lines = [line.strip() for line in lines]
    
    # Recombine, removing consecutive empty lines
    formatted_result = ""
    prev_empty = False
    for line in formatted_lines:
        if not line:
            if not prev_empty:
                formatted_result += "\n"
                prev_empty = True
        else:
            formatted_result += line + "\n"
            prev_empty = False
            
    return formatted_result

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Process the query and return results."""
    query = request.form.get('query', '')
    api_key = request.form.get('api_key', '').strip()
    
    # 检查是否提供了API密钥
    if not api_key:
        return render_template('index.html', error="API key is required to use this system.")
    
    if not query:
        return render_template('index.html', error="Please enter a query.")
    
    try:
        # 初始化框架，使用提供的API密钥
        react_framework = SimpleReActFramework(openai_api_key=api_key)
        
        # 运行查询
        result = react_framework.run(query)
        
        # Format result to improve readability
        formatted_result = format_result(result)
        
        # Log activity
        logger.info(f"Query processed: {query[:50]}...")
        
        return render_template('index.html', result=formatted_result)
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        return render_template('index.html', error=f"Error during processing: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)