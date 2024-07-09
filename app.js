window.onload = function() {
    loadPosts();
};

function loadPosts() {
    const posts = JSON.parse(localStorage.getItem('posts') || '[]');
    const postsList = document.getElementById('postsList');
    postsList.innerHTML = '';
    posts.forEach((post, index) => {
        const postElement = document.createElement('li');
        postElement.innerHTML = `
            <p>${post.content}</p>
            <textarea id="replyContent${index}" placeholder="Antworte auf diesen Beitrag..."></textarea>
            <button class="btn" onclick="replyToPost(${index})">Antworten</button>
            <ul>
                ${post.replies.map(reply => `<li>${reply}</li>`).join('')}
            </ul>
        `;
        postsList.appendChild(postElement);
    });
}

function newPost() {
    const content = document.getElementById('postContent').value;
    if (content) {
        const posts = JSON.parse(localStorage.getItem('posts') || '[]');
        posts.push({ content, replies: [] });
        localStorage.setItem('posts', JSON.stringify(posts));
        loadPosts();
        document.getElementById('postContent').value = '';
    }
}

function replyToPost(index) {
    const replyContent = document.getElementById(`replyContent${index}`).value;
    if (replyContent) {
        const posts = JSON.parse(localStorage.getItem('posts'));
        posts[index].replies.push(replyContent);
        localStorage.setItem('posts', JSON.stringify(posts));
        loadPosts();
    }
}
