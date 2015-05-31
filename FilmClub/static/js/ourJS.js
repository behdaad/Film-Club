$('.film.popup').popup({});
$('#notificationsItem').popup({
  on: 'click',
  inline: true,
  transition: 'fade down'
});

$('#searchIcon').click(
  function()
  {
    $('#searchForm').submit();
  }
);

var liked1 = false;

$('#likeButton1').click(
  function()
  {
    var count1 = parseInt($('#likeCount1').text());
    if (!liked1)
    {
      $('#likeCount1').text(String(count1 + 1));
      liked1 = true;
      $('#likeButton1').html(
        '<i class="thumbs outline down icon"></i>Unlike'
      );
    }
    else
    {
      $('#likeCount1').text(String(count1 - 1));
      liked1 = false;
      $('#likeButton1').html(
        '<i class="thumbs outline up icon"></i>Like'
      );
    }
  }
);

$('#commentButton1').click(
  function()
  {
    var text = $('#commentText1').val(); // comment text
    if (text !== "")
    {
      $('#comments1').prepend(

      '<div class="comment"> \
        <a class="avatar"> \
          <img src="img/avatar/steve.jpg"> \
        </a> \
        <div class="content"> \
          <a class="author" href="userProfile.html">Steve Jobs</a> \
          <div class="metadata"> \
            <span class="date">Just Now</span> \
          </div> \
          <div class="text">'
            + text + 
          '</div> \
        </div> \
      </div>');
      $('#commentText1').val("");
    }
    return false;
  }
);

var liked2 = false;
$('#likeButton2').click(
  function()
  {
    var count2 = parseInt($('#likeCount2').text());
    if (!liked2)
    {
      $('#likeCount2').text(String(count2 + 1));
      liked2 = true;
      $('#likeButton2').html(
        '<i class="thumbs outline down icon"></i>Unlike'
      );
    }
    else
    {
      $('#likeCount2').text(String(count2 - 1));
      liked2 = false;
      $('#likeButton2').html(
        '<i class="thumbs outline up icon"></i>Like'
      );
    }
  }
);

$('#commentButton2').click(
  function()
  {
    var text = $('#commentText2').val(); // comment text
    if (text !== "")
    {
      $('#comments2').prepend(

      '<div class="comment"> \
        <a class="avatar"> \
          <img src="img/avatar/steve.jpg"> \
        </a> \
        <div class="content"> \
          <a class="author" href="userProfile.html">Steve Jobs</a> \
          <div class="metadata"> \
            <span class="date">Just Now</span> \
          </div> \
          <div class="text">'
            + text + 
          '</div> \
        </div> \
      </div>');
      $('#commentText2').val("");
    }
    return false;
  }
);

var liked3 = false;
$('#likeButton3').click(
  function()
  {
    var count3 = parseInt($('#likeCount3').text());
    if (!liked3)
    {
      $('#likeCount3').text(String(count3 + 1));
      liked3 = true;
      $('#likeButton3').html(
        '<i class="thumbs outline down icon"></i>Unlike'
      );
    }
    else
    {
      $('#likeCount3').text(String(count3 - 1));
      liked3 = false;
      $('#likeButton3').html(
        '<i class="thumbs outline up icon"></i>Like'
      );
    }
  }
);

$('#commentButton3').click(
  function()
  {
    var text = $('#commentText3').val(); // comment text
    if (text !== "")
    {
      $('#comments3').prepend(

      '<div class="comment"> \
        <a class="avatar"> \
          <img src="img/avatar/steve.jpg"> \
        </a> \
        <div class="content"> \
          <a class="author" href="userProfile.html">Steve Jobs</a> \
          <div class="metadata"> \
            <span class="date">Just Now</span> \
          </div> \
          <div class="text">'
            + text + 
          '</div> \
        </div> \
      </div>');
      $('#commentText3').val("");
    }
    return false;
  }
);


var content = [
{
  title: 'Steve Jobs',
  description: 'User',
},
{
  title: 'Steve Jobs',
  description: 'Movie',
},
{
  title: 'Inside Job',
  description: 'Movie',
},
{
  title: 'The Italian Job',
  description: 'Movie',
},
{
  title: 'Enter the Matrix',
  description: 'Movie'
},
{
  title: 'Matrix Reloaded',
  description: 'Movie'
},
{
  title: 'Matrix Revolutions',
  description: 'Movie'
},
{
  title: 'Steven Wilson',
  description: 'User'
}
];

$('.ui.search').search(
{
  source: content,
  searchFields: [ 'title' ],
  transition: 'fade down'
}
);

