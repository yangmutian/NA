"""
Main entry point for the material analysis framework.
"""
from src.framework import SimpleReActFramework
from config.settings import API_KEY
from src.utils.logger import setup_logger
import argparse

logger = setup_logger("material_analysis.main")

def get_user_query():
    """Get query from command line arguments."""
    parser = argparse.ArgumentParser(description="Material Analysis Framework")
    parser.add_argument("--query", type=str, help="Query to analyze")
    parser.add_argument("--web", action="store_true", help="Start web interface")
    args = parser.parse_args()
    
    if args.web:
        # 启动Web界面
        from app import app
        app.run(debug=True)
        return None
    elif args.query:
        return args.query
    else:
        # 如果没有通过命令行提供查询，则请求用户输入
        return input("请输入您的分析查询: ")

def main():
    """Main function to initialize framework and run query."""
    logger.info("Starting material analysis application")
    
    query = get_user_query()
    
    # 如果启动Web界面，则直接返回
    if query is None:
        return
    
    # 初始化框架
    react_framework = SimpleReActFramework(openai_api_key=API_KEY)
    
    # 运行查询
    result = react_framework.run(query)
    
    # 显示结果
    print(result)
    logger.info("Application execution completed")

if __name__ == "__main__":
    main()