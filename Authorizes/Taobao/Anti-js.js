
    var n, og_isg = 0, t = 341,
        o = "isg",
        i = self,
        r = !! i.addEventListener,
        e = document.getElementsByTagName("head")[0],
        a = navigator.userAgent;

    !
        function(n) {
            function t() {
                return 4294967295 * Math.random() >>> 0
            }
            function o(n) {
                return /native code/.test(n + "")       //native code 表明这函数没有被重新定义过，是系统代码
            }
            function i(n) {
                for (var t = 0, o = 0, i = n.length; o < i; o++) t = (t << 5) - t + n.charCodeAt(o), t >>>= 0;
                return t
            }
            function e(n, t) {
                var o = n.indexOf(t);
                return -1 === o ? n : n.substr(0, o)
            }
            function a(n, t) {
                var o = n.indexOf(t);
                return -1 === o ? n : n.substr(o + t.length)
            }
            function c(n) {
                var t = n.match(m);
                if (!t) return null;
                var o = t[1];
                return s.test(o) && (o = a(o, "@"), o = e(o, ":")), o
            }
            function u(n) {
                for (var t = 0, o = n.length - 1; o >= 0; o--) t = t << 1 | 0 | +n[o];
                return t
            }
            function f(n, t, o, i) {
                r ? n.addEventListener(t, o, i) : n.attachEvent && n.attachEvent("on" + t, function() {
                    o(event)
                })
            }
            n.a = t, n.b = o, n.c = i, n.d = Date.now ||
                function() {
                    return +new Date
                }, n.e = e, n.f = a;
            var m = /^(?:https?:)?\/{2,}([^\/?#\\]+)/i,
                s = /[@:]/;
            n.g = c, n.h = u, n.i   = f
        }(n || (n = {}));
    var c;
    !
        function(t) {
            function o(n) {
                // L++, P = n.isTrusted == undefined || n.isTrusted, I = n.clientX, O = n.clientY
                L++, P = true, I = n.clientX, O = n.clientY //修改
            }
            function i(n) {
                T++
            }
            function r(n) {
                C++
            }
            function a(n) {
                E++
            }
            function c() {
                var n = screen.availWidth,
                    t = window.outerWidth;
                null == t && (t = document.documentElement.clientWidth || document.body.clientWidth), z = n - t < 20
            }
            function u(n) {
                A = !0, R = !0
            }
            function f(n) {
                R = !1
            }
            function m() {
                n.i(document, "mousemove", i, !0), n.i(document, "touchmove", i, !0), n.i(document, "click", o, !0), n.i(document, "keydown", a, !0);
                var t = "onwheel" in e ? "wheel" : "onmousewheel" in document ? "mousewheel" : "DOMMouseScroll";
                n.i(document, t, r, {
                    capture: !0,
                    passive: !0
                }), n.i(window, "focus", u), n.i(window, "blur", f), n.i(window, "resize", c), c(), navigator.getBattery && (B = !0, navigator.getBattery().then(function(n) {
                    M = n
                })["catch"](function(n) {})), n.i(window, "deviceorientation", function(n) {
                    $ = n.gamma
                })
            }
            function s() {
                return T
            }
            function l() {
                return C
            }
            function h() {
                return L
            }
            function v() {
                return E
            }
            function d() {
                return {
                    o: I,
                    p: O,
                    q: P
                }
            }
            function p() {
                var n = document.hidden;
                return null == n && (n = document.mozHidden), !n
            }
            function g() {
                return R
            }
            function b() {
                return A
            }
            function y() {
                return z
            }
            function w() {
                return B
            }
            function _() {
                return !M || M.charging
            }
            function j() {
                return M ? 100 * M.level : 127
            }
            function k() {
                return null != $
            }
            function x() {
                return k() ? $ + 90 : 255
            }
            var z = true, A = !0, M, T = Math.floor(Math.random()*1000), // 修改  默认为0
                L = Math.floor(Math.random()*50),  // 修改  默认为0
                C = Math.floor(Math.random()*200),									// 修改  默认为0
                E = Math.floor(Math.random()*20),
                I = Math.floor(Math.random()*1024),
                O = Math.floor(Math.random()*1024),
                P = !0,
                R = !0,
                B = !1,
                $ = null;
            t.j = m, t.k = s, t.l = l, t.m = h, t.n = v, t.r = d, t.s = p, t.t = g, t.u = b, t.v = y, t.w = w, t.x = _, t.y = j, t.z = k, t.A = x
        }(c || (c = {}));
    var u;
    !
        function(t) {
            function o() {
                // return "$cdc_asdjflasutopfhvcZLmcfl_" in document || navigator.webdriver  //chrome webdriver 会生成$cdc_asdjflasutopfhvcZLmcfl_这个对象
                return false   //修改
            }
            function u() {
                if (f()) return !1;             //判断是否手机浏览器中的事件?
                try {

                    // return !!document.createElement("canvas").getContext("webgl")
                    return true         //修改
                } catch (n) {
                    return !0
                }
            }
            function f() {
                return "ontouchstart" in document
            }
            function m() {
                // return /zh-cn/i.test(navigator.language || navigator.systemLanguage)
                return true     //修改
            }
            function s() {
                return -480 === (new Date).getTimezoneOffset()
            }
            function l() {
                return !0
            }
            function h() {
                return c.z()
            }
            function v() {
                return c.w()
            }
            function d() {
                return c.x()
            }
            function p() {
                for (var t = 0; t < 4; t++) _[5 + t] = k[t]();              //里面执行了些反扒的fun
                return n.h(_)
            }
            function g() {
                // for (var n in L) if (L.hasOwnProperty(n)) {
                //     var t = L[n];
                //     if (t()) return +n.substr(1)
                // }
                var ntjtow = 10
                for (var n in L) if (L.hasOwnProperty(n)) {              //修改 (随便返回)
                    var t = L[n];                                        //返回L中检测到的函数的编号
                    if (Math.random() * 100 < ntjtow) return +n.substr(1)
                    ntjtow = ntjtow + 5
                }
                return 0
            }
            function b(n) {
                var t = i.RTCPeerConnection || i.mozRTCPeerConnection || i.webkitRTCPeerConnection;
                if (!t) return void n(0);
                var o = {
                        optional: [{
                            D: !0
                        }]
                    },
                    r = {
                        iceServers: [{
                            urls: "stun:x"
                        }]
                    },
                    e = new t(r, o);
                setTimeout(function(n) {
                    try {
                        e.close()
                    } catch (t) {}
                }, 5e3), e.onicecandidate = function(t) {
                    var o = t.candidate;
                    if (!o) return void n(0);
                    var i = y(o.candidate);
                    null != i && (n(i), e.onicecandidate = null)
                }, e.createDataChannel(""), e.createOffer().then(function(n) {
                    e.setLocalDescription(n)
                })["catch"](function(t) {
                    n(0)
                })
            }
            function y(n) {
                var t = /(\d+)\.(\d+)\.(\d+)\.(\d+)\D/.exec(n);
                return t ? (+t[1] << 24 | +t[2] << 16 | +t[3] << 8 | +t[4]) >>> 0 : null
            }
            function w() {
                for (var n = 0; n < 5; n++) _[n] = j[n]()  //执行了一些反扒的关键
            }
            var _ = Array(16),
                j = [o, u, f, m, s],  //执行了一些反扒的关键
                k = [l, h, v, d];
            t.B = p;
            var x = navigator.vendor,
                z = e.style,
                // A = "chrome" in window, 修改
                A = false
            M = "ActiveXObject" in window,
                T = n.b(i.WeakMap),
                L = {                                                                                   //这些也是反扒的关键
                    // _13: function() {
                    //     return "callPhantom" in i || /PhantomJS/i.test(a)
                    // },
                    // _14: function() {
                    //     return /python/i.test(navigator.appVersion)
                    // },
                    _15: function() {
                        return "sgAppName" in navigator
                    },
                    _16: function() {
                        return /Maxthon/i.test(x)
                    },
                    _17: function() {
                        return "opr" in i
                    },
                    _18: function() {
                        return A && /BIDUBrowser/i.test(a)
                    },
                    _19: function() {
                        return A && /LBBROWSER/i.test(a)
                    },
                    _20: function() {
                        return A && /QQBrowser/.test(a)
                    },
                    _21: function() {
                        return A && /UBrowser/i.test(a)
                    },
                    _22: function() {
                        return A && /2345Explorer/.test(a)
                    },
                    _23: function() {
                        return A && /TheWorld/.test(a)
                    },
                    _24: function() {
                        return A && "MSGesture" in i
                    },
                    _26: function() {
                        return "aef" in i && /WW_IMSDK/.test(a)
                    },
                    _25: function() {
                        return "aef" in i
                    },
                    _1: function() {
                        return A
                    },
                    _2: function() {
                        return "mozRTCIceCandidate" in i || "mozInnerScreenY" in i
                    },
                    _3: function() {
                        return "safari" in i
                    },
                    _4: function() {
                        return M && !("maxHeight" in z)
                    },
                    _5: function() {
                        return M && !n.b(i.postMessage)
                    },
                    _6: function() {
                        return M && !r
                    },
                    _7: function() {
                        return M && !n.b(i.Uint8Array)
                    },
                    _8: function() {
                        return M && !T
                    },
                    _9: function() {
                        return M && T
                    },
                    _10: function() {
                        return "Google Inc." === navigator.vendor
                    },
                    _11: function() {
                        return "Apple Computer, Inc." === navigator.vendor
                    },
                    _12: function() {
                        return M
                    }
                };
            t.C = g, t.F = b, t.j = w
        }(u || (u = {}));
    var f, m = function() {  //设置cookie的
        function n(n) {
            this.G = new RegExp("(?:^|; )" + n + "=([^;]+)", "g"), this.H = n + "=", this.I = ""
        }
        return n.prototype.J = function() {
            for (var n, t = document.cookie, o = []; n = this.G.exec(t);) o.push(n[1]);             //根据this.G的正则 取上一次的cookie
            return o
        }, n.prototype.K = function() {
            return this.J()[0]
        }, n.prototype.L = function(n) {
            if (!this.I) {
                var t = "";
                this.M && (t += "; domain=" + this.M), this.N && (t += "; path=" + this.N), this.O && (t += "; expires=" + this.O), this.I = t
            }
            document.cookie = this.H + n + this.I
            og_isg = this.H + n + this.I //修改
        }, n.prototype.P = function() {
            var n = this.O;
            this.Q("Thu, 01 Jan 1970 00:00:00 GMT"), this.L(""), this.Q(n)       //设置cookie 了
        }, n.prototype.R = function(n) {
            this.M = n, this.I = ""                 //this.M 是cookie domain
        }, n.prototype.S = function(n) {
            this.N = n, this.I = ""
        }, n.prototype.Q = function(n) {
            this.O = n, this.I = ""                 //过期时间
        }, n
    }();
    !
        function(n) {
            function t() {
                n.T = o("95095.com,a-isv.org,aliapp.org,alibaba-inc.com,alibaba.com,alibaba.net,alibabacapital.com,alibabacloud.com,alibabacorp.com,alibabadoctor.com,alibabagroup.com,alicdn.com,alidayu.com,aliexpress.com,alifanyi.com,alihealth.cn,alihealth.com.cn,alihealth.hk,alikmd.com,alimama.com,alimei.com,alios.cn,alipay-corp.com,alipay.com,aliplus.com,alisoft.com,alisports.com,alitianji.com,alitrip.com,alitrip.hk,aliunicorn.com,aliway.com,aliwork.com,alixiaomi.com,aliyun-inc.com,aliyun.com,aliyun.xin,aliyuncs.com,alizhaopin.com,amap.com,antfinancial-corp.com,antsdaq-corp.com,asczwa.com,atatech.org,autonavi.com,b2byao.com,bcvbw.com,cainiao-inc.cn,cainiao-inc.com,cainiao.com,cainiao.com.cn,cainiaoyizhan.com,cheng.xin,cibntv.net,cnzz.com,damai.cn,ddurl.to,dingding.xin,dingtalk.com,dingtalkapps.com,doctoryou.ai,doctoryou.cn,dratio.com,etao.com,feizhu.cn,feizhu.com,fliggy.com,fliggy.hk,freshhema.com,gaode.com,gein.cn,gongyi.xin,guoguo-app.com,hemaos.com,heyi.test,hichina.com,itao.com,jingguan.ai,jiyoujia.com,juhuasuan.com,koubei-corp.com,kumiao.com,laifeng.com,laiwang.com,lazada.co.id,lazada.co.th,lazada.com,lazada.com.my,lazada.com.ph,lazada.sg,lazada.vn,liangxinyao.com,lingshoujia.com,lwurl.to,mashangfangxin.com,mashort.cn,mdeer.com,miaostreet.com,mmstat.com,mshare.cc,mybank-corp.cn,nic.xin,pailitao.com,phpwind.com,phpwind.net,saee.org.cn,shenjing.com,shyhhema.com,sm.cn,soku.com,tanx.com,taobao.com,taobao.org,taopiaopiao.com,tb.cn,tmall.com,tmall.hk,tmall.ru,tmjl.ai,tudou.com,umeng.co,umeng.com,umengcloud.com,umsns.com,umtrack.com,wasu.tv,whalecloud.com,wrating.com,www.net.cn,xiami.com,ykimg.com,youku.com,yowhale.com,yunos-inc.com,yunos.com,yushanfang.com,zmxy-corp.com.cn,zuodao.com"), n.U = o("127.0.0.1,afptrack.alimama.com,aldcdn.tmall.com,delivery.dayu.com,hzapush.aliexpress.com,local.alipcsec.com,localhost.wwbizsrv.alibaba.com,napi.uc.cn,sec.taobao.com,un.alibaba-inc.com,utp.ucweb.com,ynuf.aliapp.org"), n.V = o("alicdn.com,aliimg.com,alimama.cn,alimmdn.com,alipay.com,alivecdn.com,aliyun.com,aliyuncs.com,amap.com,autonavi.com,cibntv.net,cnzz.com,facebook.com,googleapis.com,greencompute.org,lesiclub.cn,linezing.com,mmcdn.cn,mmstat.com,sm-tc.cn,sm.cn,soku.com,tanx.com,taobaocdn.com,tbcache.com,tbcdn.cn,tudou.com,uczzd.cn,umeng.com,wrating.com,xiami.net,xiaoshuo1-sm.com,ykimg.com,youku.com,zimgs.cn")
            }
            function o(n) {
                for (var t = {}, o = n.split(","), i = 0; i < o.length; i++) t[o[i]] = !0;
                return t
            }
            n.j = t
        }(f || (f = {}));
    var s;
    !
        function(n) {
            function o(n) {
                i(n.stack || n.message)
            }
            function i(n) {
                var o = document._sufei_log;
                null == o && (o = .001), Math.random() > o || e({       //最终只是执行function e
                    code: 1,
                    msg: (n + "").substr(0, 1e3),
                    pid: "sufeidata",
                    page: location.href.split(/[#?]/)[0],
                    query: location.search.substr(1),
                    hash: location.hash,
                    referrer: document.referrer,
                    title: document.title,
                    ua: navigator.userAgent,
                    rel: t
                }, "//gm.mmstat.com/fsp.1.1?")
            }
            function r(n, t, o, i) {

                n = (n || "").substr(0, 2e3), e({
                    url: n,
                    token: t,
                    cna: o,
                    ext: i
                }, "https://fourier.alibaba.com/ts?")
            }
            function e(n, t) {
                var o = [];
                for (var i in n) o.push(i + "=" + encodeURIComponent(n[i]));
                (new Image).src = t + o.join("&")    // 带着参数 请求了gm.mmstat.com/fsp.1.1?
            }
            n.W = o, n.X = i, n.Y = r
        }(s || (s = {}));
    var l;
    !
        function(n) {
            function t(n, t, o) {
                switch (o.length) {
                    case 0:
                        return t();
                    case 1:
                        return t(o[0]);
                    case 2:
                        return t(o[0], o[1]);
                    default:
                        return t(o[0], o[2], o[3])
                }
            }
            function o(n, t) {
                switch (t.length) {
                    case 0:
                        return new n;
                    case 1:
                        return new n(t[0]);
                    case 2:
                        return new n(t[0], t[1]);
                    default:
                        return new n(t[0], t[2], t[3])
                }
            }
            function i(i, r, e) {
                return function() {
                    var a, c = arguments;
                    try {
                        a = r(c, this, i)
                    } catch (u) {
                        a = c, s.W(u)
                    }
                    if (a) {
                        if (a === n.Z) return;
                        c = a
                    }
                    return e ? o(i, c) : "apply" in i ? i.apply(this, c) : t(this, i, c)
                }
            }
            function e(n, t, o) {
                if (!n) return !1;
                var r = n[t];
                return !!r && (n[t] = i(r, o, !1), !0)
            }
            function a(n, t, o) {
                if (!n) return !1;
                var r = n[t];
                return !!r && (n[t] = i(r, o, !0), !0)
            }
            function c(n, t, o) {
                if (!u) return !1;
                var e = u(n, t);
                return !(!e || !e.set || (e.set = i(e.set, o, !1), r || (e.get = function(n) {
                    return function() {
                        return n.call(this)
                    }
                }(e.get)), Object.defineProperty(n, t, e), 0))
            }
            n.Z = -1;
            var u = Object.getOwnPropertyDescriptor;
            n.$ = e, n._ = a, n.aa = c
        }(l || (l = {}));
    var h, v = function() {
        function n(n) {
            this.ba = n;
            for (var t = 0, o = n.length; t < o; t++) this[t] = 0
        }
        return n.prototype.ca = function() {
            for (var n = this.ba, t = [], o = -1, i = 0, r = n.length; i < r; i++) for (var e = this[i], a = n[i], c = o += a; t[c] = 255 & e, 0 != --a;)--c, e >>= 8;
            return t
        }, n.prototype.da = function(n) {
            for (var t = this.ba, o = 0, i = 0, r = t.length; i < r; i++) {
                var e = t[i],
                    a = 0;
                do {
                    a = a << 8 | n[o++]
                } while (--e > 0);
                this[i] = a >>> 0
            }
        }, n
    }();
    !
        function(n) {
            function t(n) {
                for (var t = 0, o = 0, i = n.length; o < i; o++) t = (t << 5) - t + n[o];
                return 255 & t
            }
            function o(n, t, o, i, r) {
                for (var e = n.length; t < e;) o[i++] = n[t++] ^ 255 & r, r = ~ (131 * r)
            }
            function i(n) {
                for (var t = [], o = n.length, i = 0; i < o; i += 3) {
                    var r = n[i] << 16 | n[i + 1] << 8 | n[i + 2];
                    t.push(f.charAt(r >> 18), f.charAt(r >> 12 & 63), f.charAt(r >> 6 & 63), f.charAt(63 & r))
                }
                return t.join("")
            }
            function r(n) {
                for (var t = [], o = 0; o < n.length; o += 4) {
                    var i = m[n.charAt(o)] << 18 | m[n.charAt(o + 1)] << 12 | m[n.charAt(o + 2)] << 6 | m[n.charAt(o + 3)];
                    t.push(i >> 16, i >> 8 & 255, 255 & i)
                }
                return t
            }
            function e() {
                for (var n = 0; n < 64; n++) {
                    var t = f.charAt(n);
                    m[t] = n
                }
            }
            function a(n) {
                var r = t(n),
                    e = [u, r];
                return o(n, 0, e, 2, r), i(e)
            }
            function c(n) {
                var i = r(n),
                    e = i[1],
                    a = [];
                if (o(i, 2, a, 0, e), t(a) == e) return a
            }
            var u = 4,
                f = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_",
                m = {};
            n.j = e, n.ea = a, n.fa = c
        }(h || (h = {}));
    var d;
    !
        function(n) {
            function t() {
                // for (var n = navigator.platform, t = 0; t < o.length; t++) if (o[t].test(n)) return t + 1;  //修改
                // return 0
                return Math.floor(Math.random()*(o.length +1 )) //修改  //修改 (随便返回)
            }
            // var o = [/^Win32/, /^Win64/, /^Linux armv|Android/, /^Android/, /^iPhone/, /^iPad/, /^MacIntel/, /^Linux [ix]\d+/, /^ARM/, /^iPod/, /^BlackBerry/];
            var o = [/^Win32/, /^Win64/];//修改
            n.ga = t
        }(d || (d = {}));
    var p;
    !
        function(t) {
            function o() {
                // return n.d() / 1e3 >>> 0
                // return n.d() / 1e3 >>> 0 + Math.floor(Math.random() * 5000000)    //修改
                return n.d() / 1e3 >>> 0 + 100000    //修改
            }
            function i(t) {
                if (c.j(), u.j(), t) {                   //c.j() 这个就是增加事件 就是80行那里的m  ;u.j对应的是 234行的 w方法
                    var o = h.fa(t);
                    o && e.da(o)
                }
                e[1] = n.a(), e[5] = u.C(), e[6] = d.ga(), e[8] = n.c(navigator.userAgent);         //navigator.userAgent需要修改    //这里也是指纹收集
                try {
                    u.F(function(n) {
                        e[7] = n
                    })
                } catch (i) {
                    e[7] = 0
                }
            }
            function r(t, i) {  //假，真  //!!!这里很可能是收集指纹的！
                0 == e[4] && (e[4] = n.a(), e[3] = o()), e[2] = o(), e[16] = u.B(), e[9] = c.k(), e[10] = c.l(), e[11] = c.m(), e[12] = c.n(), e[17] = c.A(), e[18] = c.y();  //c.k是鼠标移动的  c.l是鼠标经过元素  c.m 鼠标点击次数  c.n键盘按下的次数  c.A 设备的方向  c.y设备电量
                var r = c.r();
                e[13] = r.o, e[14] = r.p;                    //o:点击位置的x坐标  p:点击位置的y坐标 q:这个操作是否是由用户发起的
                var f = c.t(),                              //键盘焦点是否被移开
                    m = c.v(),                              //计算浏览器宽是否在屏幕差20之内
                    s = c.u(),                              // 计算windows 有没有接收到keyboard focus 不计算窗口弹出
                    l = [i, c.s(), t, f, r.q, history.length > 1, s, m];         //c.s window是否有被用户查看
                t && a++, e[15] = n.h(l), e[0] = a;                             // n.h(l) 遍历l
                var v = e.ca();
                return h.ea(v)
            }
            var e = new v([2, 2, 4, 4, 4, 1, 1, 4, 4, 3, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1]),
                a = 0;
            t.j = i, t.ha = r
        }(p || (p = {}));
    var g;
    !
        function(t) {
            function r(n, t) {
                var o = n.split("."),
                    i = o.length - 1,
                    r = o[i];
                if (r in t) return !0;
                for (var e = i - 1; e >= 0; e--) if ((r = o[e] + "." + r) in t) return !0;
                return !1
            }
            function e(n) {
                // var t = location.hostname;
                var t = 'item.taobao.com';//修改
                do {
                    if (_.test(t)) {
                        y.L(n);
                        break
                    }
                    var o = t.split("."),
                        i = o.length;
                    if (1 === i) {
                        y.L(n);
                        break
                    }
                    i > 5 && (i = 5), t = o.pop();
                    for (var r = 2; r <= i && (t = o.pop() + "." + t, y.R(t), y.L(n), y.K() !== n); r++);
                } while (0);
                var e = "(^|\\.)" + t.replace(/\./g, "\\.") + "$";
                b = new RegExp(e, "i")
            }
            function a() {
                w = null;
                var n = p.ha(!1, null);
                y.L(n)                      //cookie的入口
            }
            function c() {
                var n = p.ha(!0);
                y.L(n), null == w && (w = setTimeout(a, 0))
            }
            function u(n, t) {
                /^\/\//.test(n) && (n = location.protocol + n);
                var o = p.ha(!0);
                null == j && (j = new m("cna").K() || ""), s.Y(n, o, j, t)
            }
            function l(n, t) {
                if (t) for (var o = 0; o < t.length; o++) if (t[o].test(n)) return !0;
                return !1
            }
            function h(t) {
                var o;
                if (null != t && (t += "", o = n.g(t)), !o) return c(), !0;
                if (b.test(o)) return c(), !0;
                if (_.test(o)) return !1;
                var e = n.e(t, "?");
                return l(e, i.__sufei_point_list) ? (u(t, 0), !1) : !(r(o, f.V) || o in f.U || /\/gw-open\/|\/gw\//.test(e) || l(e, i.__sufei_ignore_list) || (u(t, 0), 1))
            }
            function v(t) {
                var o = document.referrer;
                do {
                    if (!o) break;
                    var i = n.g(o);
                    if (!i) break;
                    if (r(i, f.T)) return
                } while (0);
                u(o, 1)
            }
            function d() {
                // for (var n = location.hostname.split("."), t = n.pop();;) {         //分割host

                for (var n = 'www.taobao.com'.split("."), t = n.pop();;) {         //修改
                    var o = n.pop();
                    if (!o) break;
                    t = o + "." + t, y.R(t), y.P()
                }
            }

            function g() {
                f.j(), y = new m(o);
                // var t = new Date(n.d() + 15552e6).toUTCString();
                var t = new Date(n.d() + 15552e6 + Math.floor(Math.random() * 5000000)).toUTCString(); //修改
                y.Q(t), y.S("/");
                var i = y.J();
                i.length > 1 && (s.X("exist_multi_isg"), d());   //如果i.length >1则不执行后面
                var r = i[0];
                p.j(r), r = p.ha(!1, null), e(r), 0 === i.length && v(r), n.i(window, "unload", function(n) {   //cookie的入口2            //有几种设置cookie的情况
                    var t = p.ha(!1, !0);                                       //在window onunload的状态  取得所有指纹
                    y.L(t)                                                      //正式设置cookie
                })
            }
            var b, y, w, _ = /^(\d+\.)*\d+$/;
            t.ia = c;
            var j;
            t.ja = h, t.j = g
        }(g || (g = {}));
    var b;
    !
        function(n) {
            function t() {
                o() || (r("insertBefore"), r("appendChild"))
            }
            function o() {
                var n = i.HTMLScriptElement;
                if (!n) return !1;
                var t = n.prototype,
                    o = /^src$/i;
                return l.$(t, "setAttribute", function(n) {
                    var t = n[0],
                        i = n[1];
                    o.test(t) && c(i)
                }), l.aa(t, "src", function(n) {
                    c(n[0])
                })
            }
            function r(n) {
                var t = i.Element;
                t ? l.$(t.prototype, n, a) : (l.$(e, n, a), l.$(document.body, n, a))
            }
            function a(n) {
                var t = n[0];
                t && "SCRIPT" === t.tagName && c(t.src)
            }
            function c(n) {
                n += "", u.test(n) && g.ja(n)
            }
            n.j = t;
            var u = /callback=/
        }(b || (b = {}));
    var y;
    !
        function(t) {
            function o(t) {
                return n.e(t.href, "#")
            }
            function r(n) {
                var t = n.target;
                if (!t) {
                    var o = m[0];
                    o && (t = o.target)
                }
                return t
            }
            function e(n) {
                if (/^https?\:/.test(n.protocol)) {
                    var t = r(n);
                    if ((!t || /^_self$/i.test(t)) && o(n) === f && n.hash) return;
                    g.ja(n.href)
                }
            }
            function a(n) {
                if (!n.defaultPrevented) for (var t = n.target || n.srcElement; t;) {
                    var o = t.tagName;
                    if ("A" === o || "AREA" === o) {
                        e(t);
                        break
                    }
                    t = t.parentNode
                }
            }
            function c(n) {
                var t = n.target || n.srcElement;   //ie下支持e.srcElement，ff支持e.target。
                t[s] !== h && g.ja(t.action)
            }
            function u() {
                m = document.getElementsByTagName("base"), f = o(location), n.i(document, "click", a), n.i(document, "submit", c);
                var t = i.HTMLFormElement;
                t && l.$(t.prototype, "submit", function(n, t) {
                    var o = t;
                    g.ja(o.action), o[s] = ++h
                })
            }
            var f, m, s = "__sufei_id",
                h = 0;
            t.j = u
        }(y || (y = {}));
    var w;
    !
        function(t) {
            function o() {
                r(), /Mobile/.test(a) && (e(), c() || n.i(document, "DOMContentLoaded", c))
            }
            function r() {
                l.$(i, "fetch", function(n) {
                    var t = n[0],
                        o = n[1];
                    "string" == typeof t && g.ja(t) && (o = o || {}, o.credentials && "omit" !== o.credentials || (o.credentials = "same-origin"), n[1] = o)
                })
            }
            function e() {
                var n = i.lib;
                if (n) {
                    var t = !/taobao.com$/.test(location.hostname);
                    l.$(n.windvane, "call", function(n) {
                        if ("MtopWVPlugin" === n[0] && "send" === n[1]) {
                            var o = n[2];
                            t ? (o.ext_headers || {})["X-Sufei-Token"] = p.ha(!0) : g.ia()
                        }
                    })
                }
            }
            function c() {
                var n = i.jsbridge;
                if (n && (n = n["default"])) return l.$(n, "pushBack", function(n) {
                    "native:" === n[0] && g.ia()
                }), !0
            }
            t.j = o
        }(w || (w = {}));
    var _;
    !
        function(n) {
            function t() {
                var n = i.XMLHttpRequest;
                if (n) {
                    var t = n.prototype;
                    t ? o(t) : r()
                }
                e()
            }
            function o(n) {
                l.$(n, "open", function(n, t) {
                    var o = n[1];
                    t[a] = o
                }), l.$(n, "send", function(n, t) {
                    var o = t[a];
                    g.ja(o)
                })
            }
            function r() {
                l._(i, "XMLHttpRequest", function() {
                    g.ja()
                })
            }
            function e() {
                var n = /XMLHTTP/i;
                l._(i, "ActiveXObject", function(t) {
                    var o = t[0];
                    o && n.test(o) && g.ja()
                })
            }
            var a = "__sufei_url";
            n.j = t
        }(_ || (_ = {}));
    var j;
    !
        function(n) {
            function o() {
                h.j(), g.j(), y.j(), _.j(), w.j(), b.j()
            }
            var i = "_sufei_data2";
            !
                function() {
                    // if (!document[i]) {   //修改
                    document[i] = t;
                    try {
                        o()
                    } catch (n) {
                        s.W(n)
                    }
                    // }					//修改
                }()
        }(j || (j = {}))
    return og_isg