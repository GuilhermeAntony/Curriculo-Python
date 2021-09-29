def func():
    arquivo = open("pagina.html","w")
    arquivo.write("""
    <html lang="pt-br">
    <head>
        <style type="text/css">
        body {
            background-color: #030326; 
            background-image: url("background.jpg");
            background-repeat: no-repeat;
            background-position: center;
            color: #5a4796;
        }
        .pri{ 
            text-align: center;
            justify-content: center;                             
        }
        .pri #image{
            width: 15rem;
            height: 15rem;
            display: inline-flex;
            flex: initial;
        }  
        .imagens{
            display: flex;
        }                
        .lista{
            display: flex;
        }
        .link{
            text-decoration: none;
            margin: auto;
            padding: auto;
            list-style: none;
            display: flex;
        }
        .link img{
            width: 5rem;
            height: 5rem;
            padding: 1rem;
        }
        .link a{
            align-items: center;
            justify-content: center;
            color: #ffffff;
            padding-top: 2rem;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            font-size: small;
        }
        .experience{
            color: #06bc57;
        }
        .experience h2{
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
            color: #343fde;
        }
        </style>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">             
    </head>  
    <body>
    """)
    nome = (input("Digite seu nome Completo \n"))   
    arquivo.write("""    <div class="pri">   
            <h1> 
                {}
            </h1>
    """.format(nome))
    trabalho = input("Digite seu Cargo no Trabalho: \n")
    arquivo.write(""" 
            <h2>        
                {}
            </h2>
    """.format(trabalho))
    github = input("Digite seu Github: \n")
    arquivo.write(""" 
            <div class="imagens">      
                <ul class="lista">        
                        <li class="link">        
                            <img src="github.jpg" alt=""><a href="https://github.com/">{}</a>
                        </li>
    """.format(github))
    linkedin = input("Digite Seu LinkedIn: \n")
    arquivo.write("""        
                        <li class="link">            
                            <img src="linkedin.png" alt=""><a href="https://linkedin.com">{}</a>
                        </li>    
    """.format(linkedin))
    email= input("Digite seu Gmail: \n")
    arquivo.write("""       
                        <li class="link">            
                            <img src="gmail.png" alt=""><a href="https://mail.google.com/">{}</a>
                        </li>
                </ul>
                <img  id="image" src="eu.png" alt=""> 
            </div>                       
        </div>    
        <div class="experience" >
            <h2>Experiencias Profissionais </h2>
    """.format(email))
    
    pergunta = 1
    while (pergunta != 2):
        pergunta = int(input("""
                1- Adicionar experiência Profissional
                2- Sair
                """))
        if pergunta == 1:
            empresa = input("Digite o nome da instituição: \n")
            arquivo.write("""                                        
            <h3>Empresa: {} </h3> 
            """.format(empresa))
            cargo = input ("Digite o cargo que voce exercia: \n")
            arquivo.write("""  
            <h3>Cargo: {}</h3>
            """.format(cargo))
            data = input("Digite o período de serviço prestado: \n")
            arquivo.write("""                 
            <p>Período: {} </p>
            """.format(data))
        elif pergunta == 2:
            print("Tchau vadia!")
    arquivo.write("""
            <h2>Formações e Cursos </h2> """)
    puta = 1
    while (puta != 2): 
            puta = int(input("""
                    1- Adicionar Cursos 
                    2- Sair
                    """))
            if puta ==1:
                instituicao = (input("Digite o nome da instituição: \n"))
                arquivo.write("""                                       
            <h3>Instituição: {} </h3> 
                """.format(instituicao))
                curso = input ("Digite qual o curso realizado: \n")
                arquivo.write("""  
            <h3>Curso: {}</h3>
                """.format(curso))
                datas = input("Digite o tempo de curso: \n")
                arquivo.write("""                 
            <p>Período: {} </p>
                """.format(datas))
            elif puta == 2:
                print("Tchau vadia!")
    arquivo.write(""" 
        </div>      
    </body> 
    </html>
    """) 
    arquivo.close()
    return arquivo
func()
