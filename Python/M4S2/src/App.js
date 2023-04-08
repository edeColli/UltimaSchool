const adicionarAoCarrinho = document.getElementsByClassName('stretched-link')

for (let i = 0; i < adicionarAoCarrinho.length; i++) {
  adicionarAoCarrinho[i].addEventListener('click', () => {
    alert('Produto adicionado ao carrinho!')
  })
}
