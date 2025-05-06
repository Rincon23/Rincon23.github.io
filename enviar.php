<?php

    $nome = addslashes($_POST['nome']);
    $email =  addslashes($_POST['email']);
    $celular = addslashes($_POST['celular']);
    $mensagem = addslashes($_POST['mensagem']);

    $para = "enzorincon2003@gmail.com";
    $assunto = "Mensagem de contato - github.io";
    $corpo = "Nome: $nome\n, E-mail: $email\n, Celular: $celular\n";
    $cabeca = "From: enzo.rincon@hotmail.com \n Reply-to: $email\n X=Mailer: PHP/" . phpversion();

    if(mail($para, $assunto, $corpo, $cabeca)){
        echo "Email enviado com sucesso!";
    } else {
        echo "Erro ao enviar o email!";
    }

?>