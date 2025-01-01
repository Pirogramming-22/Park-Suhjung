//Fetch the items from Json

function loadItems(){
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}


//update list with givne item
function displayItems(items) {
    const container= document.querySelector('.items');
    const html =items.map(item => createHTMLString(item));
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

//create html list from the given data
function createHTMLString(item){
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail"/>
        <span class="item__description"> ${item.gender}, ${item.size}</span>
    </li>
    `;
}


//main
loadItems()
.then(items => {
    console.log(items);
    displayItems(items);
 //   setEventListeners(items)
})
.catch(console.log);