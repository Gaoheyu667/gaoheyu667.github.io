// 当前时间显示
function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleTimeString('zh-CN');
    document.getElementById('current-time').textContent = timeString;
}

setInterval(updateTime, 1000);
updateTime();


// 轮播图功能
const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slide');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
let currentSlide = 0;

function showSlide(index) {
    if (index >= slides.length) currentSlide = 0;
    if (index < 0) currentSlide = slides.length - 1;
    slider.style.transform = `translateX(-${currentSlide * 100}%)`;
}

prevBtn?.addEventListener('click', () => {
    currentSlide--;
    showSlide(currentSlide);
});

nextBtn?.addEventListener('click', () => {
    currentSlide++;
    showSlide(currentSlide);
});

// 自动轮播
setInterval(() => {
    currentSlide++;
    showSlide(currentSlide);
}, 5000);


// 评论功能
const commentInput = document.getElementById('comment-input');
const submitComment = document.getElementById('submit-comment');
const commentsContainer = document.getElementById('comments-container');

submitComment?.addEventListener('click', () => {
    const commentText = commentInput.value.trim();
    if (!commentText) return;

    const comment = document.createElement('div');
    comment.className = 'comment';
    comment.innerHTML = `
        <div class="comment-header">
            <div class="comment-info">
                <div class="user-name">匿名用户</div>
                <div class="rating-display">★★★☆☆</div> <!-- 新增评分 -->
            </div>
            <div class="comment-time">${new Date().toLocaleString()}</div>
        </div>
        <p class="comment-content">${commentText}</p>
        <div class="comment-actions">
            <button class="like-btn">
                <span class="like-icon">👍</span>
                <span class="like-count">0</span>
            </button>
            <button class="reply-btn">回复</button>
        </div>
    `;

    commentsContainer.insertBefore(comment, commentsContainer.firstChild);
    commentInput.value = '';
});


// 切换主图片（假设图片在 index1.html 中）
function changeMainImage(src) {
    document.querySelector('.main-image').src = src; // 需确保 index1.html 有 .main-image 元素
}


// 切换标签页（假设标签页在 index1.html 中）
function showTab(tabId) {
    // 隐藏所有标签页内容
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });

    // 移除所有标签按钮的激活状态
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    // 显示选中的标签页内容
    document.getElementById(tabId).classList.add('active');

    // 激活对应的标签按钮
    event.target.classList.add('active');
}


// 评论功能增强（新增 CSS 类引用）
document.addEventListener('DOMContentLoaded', function() {
    // 字数统计（关联 style1.css 中的 .char-count）
    const commentInput = document.getElementById('comment-input');
    const charCount = document.querySelector('.char-count');

    commentInput?.addEventListener('input', function() {
        const count = this.value.length;
        charCount.textContent = `${count}/200`;
        if (count > 200) {
            this.value = this.value.substring(0, 200);
            charCount.textContent = '200/200';
        }
    });

    // 星级评分（关联 style1.css 中的 .star.active）
    const stars = document.querySelectorAll('.star');
    let currentRating = 0;

    stars.forEach(star => {
        star.addEventListener('mouseover', function() {
            const rating = this.dataset.rating;
            highlightStars(rating);
        });

        star.addEventListener('click', function() {
            currentRating = this.dataset.rating;
            highlightStars(currentRating);
        });

        star.addEventListener('mouseout', function() {
            highlightStars(currentRating);
        });
    });

    function highlightStars(rating) {
        stars.forEach(star => {
            const starRating = star.dataset.rating;
            star.classList.toggle('active', starRating <= rating); // 依赖 style1.css 中的 .active 样式
        });
    }

    // 点赞功能（关联 style1.css 中的 --primary-color）
    const likeBtns = document.querySelectorAll('.like-btn');
    likeBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const countSpan = this.querySelector('.like-count');
            let count = parseInt(countSpan.textContent);
            countSpan.textContent = count + 1;
            this.style.color = getComputedStyle(document.documentElement).getPropertyValue('--primary-color').trim();
        });
    });
});