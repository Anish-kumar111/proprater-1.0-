var stickyEl2 = document.querySelector(".me_stickyNav")
        var stickyPosition2 = stickyEl2.getBoundingClientRect().top;
        var offset = -10
        window.addEventListener('scroll', () => {
                if (window.pageYOffset >= stickyPosition2 + offset) {
                    stickyEl2.style.position2 = 'fixed';
                    stickyEl2.style.top = '0px';
                } else {
                    stickyEl2.style.position2 = 'static';
                    stickyEl2.style.top = '';
                }
            });