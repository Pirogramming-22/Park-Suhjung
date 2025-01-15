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

function onButtonClick(event, items){
    const dataset=event.target.dataset;
    const key=dataset.key;
    const value =dataset.value;
    if (key==null || value==null){
        return;
    }

    displayItems(items.filter(item => item[key]==value))

    //updateItems(items, key, value);

}


//function updateItems(items, key, value){
//items.forEach(item)=> {
  //if(item.dataset[key]===value){ item.classList.remove('invisible');}
  //else{item.classList.add('invisible');}  
//});
//}

function setEventListeners(items)
{
    const logo =document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click',()=>displayItems(items));
    buttons.addEventListener('click',event => onButtonClick(event, items));
}

//main
loadItems()
.then(items => {
    console.log(items);
    displayItems(items);
    setEventListeners(items)
})
.catch(console.log);