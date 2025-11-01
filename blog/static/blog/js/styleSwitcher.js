const links = document.querySelectorAll('.alternate-style'),
    totalLinks = links.length;

function setActiveStyle(color) {
    for (let i = 0; i < totalLinks; i++) {
        if (color === links[i].getAttribute('title')) {
            links[i].removeAttribute('disabled');
        } else {
            links[i].setAttribute('disabled', true);
        }
    }
    // LocalStorage ga saqlash
    localStorage.setItem("activeColor", color);
}

// Page reload bo‘lganda oxirgi tanlangan rangni qo‘yish
const savedColor = localStorage.getItem("activeColor");
if (savedColor) {
    setActiveStyle(savedColor);
}

// ====================
// body skin (dark/light)
// ====================
const bodySkin = document.querySelectorAll('.body-skin'),
    totalBodySkin = bodySkin.length;

for (let i = 0; i < totalBodySkin; i++) {
    bodySkin[i].addEventListener('change', function(){
        if(this.value === 'dark'){
            document.body.className = 'dark';
            localStorage.setItem("theme", "dark");
        } else {
            document.body.className = '';
            localStorage.setItem("theme", "light");
        }
    });
}

// Page reload bo‘lganda oxirgi tanlangan theme ni qo‘yish
const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
    if (savedTheme === "dark") {
        document.body.className = 'dark';
        // inputni ham dark qilib qo‘yish kerak bo‘lsa:
        document.querySelector('.body-skin[value="dark"]').checked = true;
    } else {
        document.body.className = '';
        document.querySelector('.body-skin[value="light"]').checked = true;
    }
}

// ====================
// style switcher toggle
// ====================
document.querySelector('.toggle-style-switcher').addEventListener('click', () => {
    document.querySelector('.style-switcher').classList.toggle('open');
});
