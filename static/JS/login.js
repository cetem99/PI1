const nomes_login = [];

      const Enviar = () => {
        const nameInputValue = document.getElementById("name_input").value;
        const passwordInputValue =
          document.getElementById("password_input").value;
        const Aceitar = document.getElementById("habi").checked;
        if (!Aceitar) {
          alert("Você deve aceitar os termos de uso antes de prosseguir.");
        } else if (nameInputValue && passwordInputValue) {
          nomes_login.push({ Nome: nameInputValue, Senha: passwordInputValue });
          console.log(nomes_login);
        } else {
          alert("Preencha os campos de nome e senha antes de enviar.");
        }
      };
    