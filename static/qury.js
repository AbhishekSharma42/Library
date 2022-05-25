window.onload = initAll;

function initAll() {
    savebookbutton = document.getElementById("save_book");
    savebookbutton.onclick = saveBook;
}

function showAllBook() {
    var url = '/Api';
    var req = new XMLHttpRequest();
    req.onreadystatechange = function () {
        if (this.readyState == 4 & this.status == 200) {
            var Bname = eval(req.responseText);
            console.table(Bname);
        }
    };
    req.open("GET", url, true);
    req.send();
}

function saveBook() {
    var bookename = document.getElementById("BookName").value;
    var bookprize = document.getElementById("BookPrize").value;
    var bookpages = document.getElementById("BookPage").value;

    var url = '/save_Book?name=' + bookename + "&prize=" + bookprize + "&page=" + bookpages;

    var req = new XMLHttpRequest();
    req.onreadystatechange = function () {
        if (this.readyState == 4 & this.status == 200) {
            var data = eval(req.responseText);

            var div = document.getElementById("pills-profile");
            var table = document.createElement("table");

            for (var i = 0; i < data.length; i++) {
                var row = table.insertRow(i);
                var names = row.insertCell(0);
                var price = row.insertCell(1);
                var pages = row.insertCell(2);

                names.innerHTML = data[i].bookename;
                price.innerHTML = data[i].bookprize;
                pages.innerHTML = data[i].bookpages;
            }

            div.appendChild(table);
        }
    };
    req.open("GET", url, true);

    req.send();
}