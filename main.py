#                                           
#       Author : wang                    
#       time   : 2020/5/31:下午9:28            
#


from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], threaded=True)
