def atend(): 
    print('Olá! Seja bem-vindo ao nosso atendimento online!')
    print('1 - Atendimento por ligação.')
    print('2 - Suporte técnico à distância.')
    print('3 - Suporte técnico presencial.')
    resp = input ('Escolha uma opção.')

    if(resp == '1'):
        print('Para falar com um de nossos atendentes, ligue para 555555555')
    if(resp == '2'):
        print('Para suporte técnico à distância, ligue para 222222222')
    if(resp == '3'):
        input('Solicitaremos um de nossos técnicos para que ele possa ir até sua residência prestar todo suporte necessário. Por favor, nos informe seu endereço para que possamos agendar a visita e também nos informe um número para contato.')
    
    print('Agradecemos o seu contato!')
    print('Posso te ajudar com mais alguma coisa?')
    print('1 - Sim.')
    print('2 - Não.')
    resp = input('')

    if(resp == '1'):
        atend()    
    if(resp == '2'):
        print('Agradecemos o seu contato. Até a próxima!')