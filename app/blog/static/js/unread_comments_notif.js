const jQIconBell = $("#unread-comments-notif-btn-icon");

// when logging in via modal on a `blog.` page/opening a `blog.` page as admin, check for notifications
onSamePageLogin = addToFunction(onSamePageLogin, function() {
    updateUnreadComments();
});

$(document).ready(async function() {
    if (await IS_USER_AUTHENTICATED()) {
        updateUnreadComments();
    }
});

async function updateUnreadComments() {
    let notifCount = await updateUnreadCommentsDropdown();
    if (notifCount > 0) {
        setBellWithNotif();
    } else {
        setBellWithoutNotif();
    }
}

function setBellWithNotif() {
    jQIconBell.removeClass("bi-bell");
    jQIconBell.addClass("bi-bell-fill");
}

function setBellWithoutNotif() {
    jQIconBell.removeClass("bi-bell-fill");
    jQIconBell.addClass("bi-bell");
}

async function updateUnreadCommentsDropdown() {
    const jQDropdownUnreadComments = $("#unread-comments-dropdown");

    // get posts with unread comments
    jQDropdownUnreadComments.html('<span class="dropdown-item">Loading…</span>');
    const resp = await fetchWrapper(GET_POSTS_WITH_UNREAD_COMMENTS_URL, {method: "POST"});

    if (resp.errorStatus) {
        jQDropdownUnreadComments.html('<span class="dropdown-item">Unable to load posts :/</span>');
        return -1;
    }

    let postCount = Object.keys(resp).length;
    if (postCount === 0) {
        jQDropdownUnreadComments.html('<span class="dropdown-item">There\'s nothing here :]</span>');
        return postCount;
    }

    let html = "";
    for (const [postTitle, v] of Object.entries(resp)) {
        html +=
                `<a class="dropdown-item" href="${v.url}">` +
                  `<span class="custom-pink-light">(${v.unread_comment_count})</span>` +
                  `${postTitle}` +
                "</a>";
    }
    jQDropdownUnreadComments.html(html);

    return postCount;
}

$(document).ready(function() {
    // refresh notifications on click
    $("#unread-comments-notif-btn").on("click", function() {
        updateUnreadComments();
    });
});
