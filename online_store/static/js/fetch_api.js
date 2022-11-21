fetch('/api/books')
    .then(response => response.json())
    .then(books => createCards(books))
    .catch(err => console.log(err))

function createCards(response){
    response.forEach((item, i=0) => {
        if (i < 16){
            let book = document.createElement('div');
            book.classList.add('block_content');
            book.innerHTML = `
                <div class="block_img"><a href="#"><img class="block_img" src="/api/book/images/${item.id}" alt=""></a></div>
                <div class="title_block"><a href="#"><h3 class="title_text">${item.title}</h3></a></div>
                <div class="author_block"><a href="#"><h4>${item.author_name}</h4></a></div>
                <hr class="hr_content">
                <div class="price">
                    <img class="rub" src="static/img/russian-rouble-coin-color-icon.svg" alt="">
                    <h3>${item.price}</h3>
                    <div class="basket"><a href="#"><img class="rub" id="basket" src="static/img/icons8-продать-запас-48.png" alt=""></a></div>
                </div>
                `;
            document.querySelector(".wraper_content").appendChild(book)
            ++i
         }
    })
}





