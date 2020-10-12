function movePage(action){
    var form = document.getElementById("navigation_form");
    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);
    form.submit();
}

function moveToDetail(action, key){

    var form = document.getElementById("navigation_form");

    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);

    var elm2 = document.createElement("input");
    elm2.setAttribute("name", "key");
    elm2.setAttribute("type", "hidden");
    elm2.setAttribute("value", key);
    form.appendChild(elm2);

    form.submit();
}

function moveToDetailFromList(action, key){
    var form = document.getElementById("list_form");

    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);

    var elm2 = document.createElement("input");
    elm2.setAttribute("name", "key");
    elm2.setAttribute("type", "hidden");
    elm2.setAttribute("value", key);
    form.appendChild(elm2);

    form.submit();
}

function deleteRecord(action, key){
    var form = document.getElementById("list_form");
    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);

    var elm2 = document.createElement("input");
    elm2.setAttribute("name", "key");
    elm2.setAttribute("type", "hidden");
    elm2.setAttribute("value", key);
    form.appendChild(elm2);

    form.submit();
}

$(".tab_label").on("click",function(){
 var $th = $(this).index()+1;
 $(".tab_label").removeClass("active");
 $(".tab_panel").removeClass("active");
 $(this).addClass("active");
 $("#panel"+$th).addClass("active").appendTo($("#cj_panelarea"));
});



$('#reply_form').submit(function(event){
  //通常のアクションをキャンセルする
  event.preventDefault();
  //Formの参照を取る
  var form = $(this);
  $.ajax({
       url: form.attr('action'),
       type: form.attr('method'),
       data: form.serialize(),
       dataType: "text",
     })
     .done(function(data) {
       const parsed_data = JSON.parse(data);
       var new_reply = document.createElement('div');
       new_reply.id = 'replys';
       new_reply.className = 'row';

       var first_col = document.createElement('div');
       first_col.className = 'col-1 col-sm-2';

       var second_col = document.createElement('div');
       second_col.className = 'col-2 col-sm-2 text-center align-middle';

       var user_photo = document.createElement('img');
       user_photo.src = '/media/' + parsed_data.user_photo;
       user_photo.className = 'profile-reply img-fluid';
       second_col.appendChild(user_photo);

       var third_col = document.createElement('div');
       third_col.className = 'col-8 col-sm-6';

       var reply_area = document.createElement('div');
       reply_area.className = 'description-text text-left';

       reply_area.innerHTML = parsed_data.user_username + '<br>' + parsed_data.reply + '<br><span class="feed-info-right-sm">' + parsed_data.reply_date + '</span>';
       third_col.appendChild(reply_area);

       var forth_col = document.createElement('div');
       forth_col.className = 'col-1 col-sm-2';

       new_reply.appendChild(first_col);
       new_reply.appendChild(second_col);
       new_reply.appendChild(third_col);
       new_reply.appendChild(forth_col);

       var hr = document.createElement('div');
       hr.id = 'replys';
       hr.className = 'row';
       hr.innerHTML =  '<div class="col-3 col-sm-2"></div><div class="col-6 col-sm-8"><hr></div><div class="col-3 col-sm-2"></div>'

       document.getElementById('reply_container').appendChild(new_reply);
       document.getElementById('reply_container').appendChild(hr);

       var input_text = document.getElementById("id_reply");
       input_text.value = '';
     })
});



function like(api_url, comment_id) {
    var btn = document.getElementById("like-count-" + comment_id);
    var img = document.getElementById("comment-like-" + comment_id);
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var received_data = JSON.parse(request.responseText);
            btn.innerText = received_data.like;
            img.src = received_data.like_img;
        }
    }
    request.open("GET",api_url);
    request.send();
}

function comment_wish(api_url, comment_id) {
    var btn = document.getElementById("comment-wish-count-" + comment_id);
    var img = document.getElementById("comment-wish-" + comment_id);
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var received_data = JSON.parse(request.responseText);
            btn.innerText = received_data.wish;
            img.src = received_data.wish_img;
        }
    }
    request.open("GET",api_url);
    request.send();
}

function beer_wish(api_url, beer_id) {
    var btn = document.getElementById("wish-beer-" + beer_id);
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var received_data = JSON.parse(request.responseText);
            if (received_data.wished) {
              btn.classList.remove('btn-outline-success');
              btn.classList.add('btn-success');
              btn.innerText = "wished!";
            } else{
              btn.classList.remove('btn-success');
              btn.classList.add('btn-outline-success');
              btn.innerText = "wish listに追加";
            }
        }
    }
    request.open("GET",api_url);
    request.send();
}

function brewery_wish(api_url, brewery_id) {
    var btn = document.getElementById("wish-brewery-" + brewery_id);
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var received_data = JSON.parse(request.responseText);
            if (received_data.wished) {
              btn.classList.remove('btn-outline-success');
              btn.classList.add('btn-success');
              btn.innerText = "wish listに追加しました";
            } else{
              btn.classList.remove('btn-success');
              btn.classList.add('btn-outline-success');
              btn.innerText = "気になる！";
            }
        }
    }
    request.open("GET",api_url);
    request.send();
}

function venue_wish(api_url, venue_id) {
    var btn = document.getElementById("wish-venue-" + venue_id);
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var received_data = JSON.parse(request.responseText);
            if (received_data.wished) {
              btn.classList.remove('btn-outline-success');
              btn.classList.add('btn-success');
              btn.innerText = "wish listに追加しました";
            } else{
              btn.classList.remove('btn-success');
              btn.classList.add('btn-outline-success');
              btn.innerText = "行きたい！";
            }
        }
    }
    request.open("GET",api_url);
    request.send();
}
