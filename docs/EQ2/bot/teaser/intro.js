(function () {
	var W = 720, H = 405, FLOOR = 330, S = 0.55;           // stage size, floor line, ogre scale
	var TY = FLOOR - 324 * S;                               // ogre y offset that puts his feet on the floor
	var WIN = {                                             // the three windows, in stage px
		bot: { x: 8,   y: FLOOR - 127, w: 250, h: 127 },
		osa: { x: 262, y: FLOOR - 78,  w: 140, h: 78 },
		mcp: { x: 420, y: FLOOR - 89,  w: 200, h: 89 }
	};

	var raf = (typeof window.requestAnimationFrame === 'function')
		? function (f) { return window.requestAnimationFrame(f); }
		: function (f) { return setTimeout(function () { f(now()); }, 16); };
	function now() { return (window.performance && performance.now) ? performance.now() : new Date().getTime(); }
	function clamp(v, a, b) { return v < a ? a : (v > b ? b : v); }
	function lerp(a, b, p) { return a + (b - a) * p; }
	function easeIn(p) { return p * p * p; }
	function easeOut(p) { return 1 - Math.pow(1 - p, 3); }
	function easeIO(p) { return p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; }
	function rot(x, y, deg) { var r = deg * Math.PI / 180, c = Math.cos(r), s = Math.sin(r); return { x: x * c - y * s, y: x * s + y * c }; }

	var CSS = [
		'#tio-root{position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;background:#11161a;font-family:"Segoe UI",Tahoma,sans-serif;user-select:none;-webkit-user-select:none}',
		'#tio-root button,#tio-root button:hover{text-shadow:none;box-shadow:none;font-family:inherit;line-height:normal}',
		'#tio-root .tio-stage{position:absolute;left:0;top:0;width:720px;height:405px;transform-origin:0 0;overflow:hidden}',
		'#tio-root .tio-world{position:absolute;left:0;top:0;width:720px;height:405px}',
		'#tio-root .tio-wall{position:absolute;left:-30px;top:-30px;width:780px;height:360px;background:#46545a}',
		'#tio-root .tio-floor{position:absolute;left:-30px;top:330px;width:780px;height:105px;background:#38444a;border-top:3px solid #2a3437}',
		'#tio-root .tio-win{position:absolute;background-size:100% 100%;background-repeat:no-repeat;transform-origin:50% 100%}',
		'#tio-root .tio-tile{position:absolute;background-repeat:no-repeat}',
		'#tio-root .tio-layer{position:absolute;left:0;top:0;width:720px;height:405px;overflow:visible;pointer-events:none}',
		'#tio-root .tio-fx{position:absolute;font-weight:900;font-size:40px;color:#ffd23f;letter-spacing:1px;white-space:nowrap;pointer-events:none;opacity:0;',
		'  text-shadow:3px 3px 0 #7a2e00,-2px -2px 0 #7a2e00,2px -2px 0 #7a2e00,-2px 2px 0 #7a2e00}',
		'#tio-root .tio-dust{position:absolute;border-radius:50%;background:#d6cdb5;pointer-events:none}',
		'#tio-root .tio-key{position:absolute;font-family:Consolas,"Courier New",monospace;font-weight:700;font-size:13px;color:#7dff6a;pointer-events:none}',
		'#tio-root .tio-bubble{position:absolute;max-width:250px;background:#f6f3e8;color:#1b1b1b;font-size:15px;font-weight:700;line-height:1.3;padding:8px 12px;',
		'  border-radius:13px;border:2px solid #141414;opacity:0;pointer-events:none}',
		'#tio-root .tio-bubble:after{content:"";position:absolute;right:22px;bottom:-12px;border-style:solid;border-width:12px 10px 0 10px;border-color:#141414 transparent transparent transparent}',
		'#tio-root .tio-bubble:before{content:"";position:absolute;right:24px;bottom:-8px;border-style:solid;border-width:9px 8px 0 8px;border-color:#f6f3e8 transparent transparent transparent;z-index:1}',
		'#tio-root .tio-screen{position:absolute;left:116px;top:126px;width:208px;height:118px;overflow:hidden;font-family:Consolas,"Courier New",monospace;',
		'  font-size:9.5px;line-height:12px;color:#6dff6d;white-space:pre}',
		'#tio-root .tio-fade{position:absolute;left:0;top:0;width:720px;height:405px;background:#000;pointer-events:none}',
		'#tio-root .tio-title{position:absolute;left:0;top:0;width:720px;height:405px;background:#1a2320;text-align:center;display:none;opacity:0}',
		'#tio-root .tio-title h1{margin:0;padding-top:128px;font-size:34px;font-weight:800;color:#8ee06a}',
		'#tio-root .tio-title p{margin:10px 0 0;font-size:15px;color:#9fb59a;font-style:italic}',
		'#tio-root .tio-go{margin-top:28px;background:#2f7d22;color:#fff;border:1px solid #8ee06a;border-radius:7px;padding:9px 22px;font-size:15px;font-weight:700;cursor:pointer}',
		'#tio-root .tio-ctl{position:absolute;right:10px;top:10px;z-index:30;display:flex;flex-direction:column;align-items:stretch}',
		'#tio-root .tio-play{margin-bottom:6px;background:#2f7d22;color:#fff;border:1px solid #8ee06a;border-radius:6px;padding:5px 13px;font-size:13px;font-weight:700;cursor:pointer}',
		'#tio-root .tio-skip{position:relative;overflow:hidden;background:rgba(18,24,22,.85);color:#cfe8c2;border:1px solid #5d7f55;border-radius:6px;',
		'  padding:5px 13px;font-size:13px;font-weight:600;cursor:pointer}',
		'#tio-root .tio-fill{position:absolute;left:0;top:0;bottom:0;width:0;background:rgba(142,224,106,.4);pointer-events:none}',
		'#tio-root .tio-lbl{position:relative;pointer-events:none}',
		'#tio-root .tio-again{margin:28px 12px 0 0;background:transparent;color:#cfe8c2;border:1px solid #5d7f55;border-radius:7px;padding:9px 18px;font-size:15px;font-weight:600;cursor:pointer}',
		'#tio-root .tio-skip:hover,#tio-root .tio-go:hover,#tio-root .tio-play:hover,#tio-root .tio-again:hover{filter:brightness(1.15)}',
		'#tio-root .tio-reply{position:absolute;left:236px;top:142px;min-width:170px;display:none;opacity:0;z-index:20;cursor:pointer;',
		'  background:linear-gradient(#57503a,#3a3524 55%,#2c2819);border:2px solid #9c8a55;border-radius:4px;box-shadow:0 0 0 1px #15130c,0 3px 8px rgba(0,0,0,.5);',
		'  padding:6px 18px;font-family:Georgia,"Times New Roman",serif;font-size:16px;font-weight:700;color:#f3e8c4;text-shadow:1px 1px 0 #000;text-align:center}',
		'#tio-root .tio-reply:hover{background:linear-gradient(#6a6246,#46402b 55%,#332e1d);border-color:#c9b170}',
		'#tio-root.tio-wait{cursor:pointer}',
		'#tio-root .sk{fill:#7fae57;stroke:#141414;stroke-width:3.2;stroke-linejoin:round;stroke-linecap:round}',
		'#tio-root .wd{fill:#8a5a2b;stroke:#141414;stroke-width:3.2;stroke-linejoin:round}',
		'#tio-root .bk{fill:#141414;stroke:#141414;stroke-width:2;stroke-linejoin:round}',
		'#tio-root .ln{fill:none;stroke:#141414;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}',
		'#tio-root .lnw{fill:none;stroke:#5a3a1a;stroke-width:2;stroke-linecap:round}',
		'#tio-root .br{fill:none;stroke:#141414;stroke-width:5;stroke-linecap:round}',
		'#tio-root .tu{fill:#f3ecd6;stroke:#141414;stroke-width:2.4;stroke-linejoin:round}'
	].join('\n');

	var CLUB =
		'<path class="wd" d="M77 212 L79 224 L84 216 L88 228 L92 214 L97 224 L99 210 L103 200 L20 28 L3 12 L4 27 L9 45 L-4 34 L-12 26 L-12 44 Z"/>' +
		'<path class="ln" d="M9 45 C26 80 40 110 52 134"/>' +
		'<path class="lnw" d="M4 60 C22 96 38 128 54 158 M30 40 C48 78 64 110 80 142"/>';

	var OGRE =
		'<g id="tio-ogre"><g id="tio-body">' +
		 '<g id="tio-legs">' +
		  '<g id="tio-legL">' +
		   '<path class="sk" d="M202 186 C178 184 152 198 142 222 C134 244 140 262 158 262 C176 258 192 238 208 210 Z"/>' +
		   '<path class="sk" d="M140 250 C130 270 134 292 146 304 L178 304 C180 286 178 266 168 254 Z"/>' +
		   '<path class="ln" d="M152 272 C158 282 162 292 160 300 M162 214 C170 226 172 238 168 248"/>' +
		   '<path class="sk" d="M126 304 C122 294 140 290 158 292 C174 294 188 298 190 306 C190 316 174 318 150 318 C134 318 124 312 126 304 Z"/>' +
		   '<path class="ln" d="M137 307 L137 316 M148 307 L148 318 M159 307 L159 318 M170 307 L170 317 M180 307 L180 315"/>' +
		  '</g>' +
		  '<g id="tio-legR">' +
		   '<path class="sk" d="M240 186 C264 184 290 198 300 222 C308 244 302 262 284 262 C266 258 250 238 234 210 Z"/>' +
		   '<path class="sk" d="M302 250 C312 270 308 292 296 304 L264 304 C262 286 264 266 274 254 Z"/>' +
		   '<path class="ln" d="M290 272 C284 282 280 292 282 300 M280 214 C272 226 270 238 274 248"/>' +
		   '<path class="sk" d="M256 308 C256 296 274 294 294 296 C312 298 324 304 322 314 C320 322 302 324 280 324 C264 324 256 318 256 308 Z"/>' +
		   '<path class="ln" d="M267 311 L267 321 M278 311 L278 323 M289 311 L289 323 M300 311 L300 322 M311 311 L311 320"/>' +
		  '</g>' +
		  '<path class="bk" d="M204 198 L238 198 L244 234 L221 244 L198 234 Z"/>' +
		 '</g>' +
		 '<path class="sk" d="M160 96 C170 84 200 86 220 88 C242 86 270 84 280 96 C286 118 276 142 262 160 C256 172 250 180 244 186 L198 186 C190 178 184 170 178 160 C164 142 154 118 160 96 Z"/>' +
		 '<path class="ln" d="M172 108 C186 128 204 130 212 120 M228 120 C236 130 254 128 268 108"/>' +
		 '<path class="ln" d="M194 150 C200 158 204 164 206 172 M246 150 C240 158 236 164 234 172"/>' +
		 '<path class="sk" d="M188 178 C206 186 234 186 254 178 L256 192 C236 200 206 200 186 192 Z"/>' +
		 '<path class="bk" d="M200 196 L242 196 L236 212 L221 220 L206 212 Z"/>' +
		 '<path class="bk" d="M162 106 C156 124 150 136 140 142 C150 150 164 154 180 160 C170 142 166 124 168 106 Z"/>' +
		 '<path class="bk" d="M278 106 C284 124 290 136 300 142 C290 150 276 154 260 160 C270 142 274 124 272 106 Z"/>' +
		 '<path class="sk" d="M198 58 C176 56 152 64 136 80 C146 98 172 98 198 90 Z"/>' +
		 '<path class="sk" d="M242 58 C264 56 288 64 304 80 C294 98 268 98 242 90 Z"/>' +
		 '<g id="tio-armR">' +
		  '<path class="sk" d="M302 102 C324 98 340 116 336 138 C332 150 316 152 306 144 Z"/>' +
		  '<ellipse class="sk" cx="292" cy="94" rx="29" ry="27"/>' +
		  '<path class="sk" d="M300 120 C318 124 330 140 326 156 C314 162 298 156 292 144 Z"/>' +
		  '<path class="sk" d="M272 150 C274 134 298 128 316 134 C334 140 338 160 332 176 C326 190 304 194 288 188 C274 182 270 166 272 150 Z"/>' +
		  '<path class="ln" d="M287 140 C285 154 285 172 287 184 M302 136 C300 150 300 172 302 188 M317 140 C315 154 315 170 317 182 M276 154 C290 148 310 150 330 158"/>' +
		 '</g>' +
		 '<g id="tio-armL">' +
		  '<g id="tio-club">' + CLUB + '</g>' +
		  '<ellipse class="sk" cx="146" cy="94" rx="29" ry="27"/>' +
		  '<path class="sk" d="M116 112 C112 90 132 78 152 86 C164 100 158 124 140 134 C126 138 116 128 116 112 Z"/>' +
		  '<path class="sk" d="M84 134 C94 116 118 108 130 116 C136 130 126 152 104 164 Z"/>' +
		  '<path class="ln" d="M100 128 C108 124 116 124 122 128"/>' +
		  '<path class="sk" d="M42 150 C38 130 60 124 80 128 C98 130 106 146 102 164 C100 180 86 188 66 186 C48 184 42 172 42 150 Z"/>' +
		  '<path class="ln" d="M57 137 C55 150 55 170 57 182 M71 131 C69 146 69 170 71 185 M86 134 C84 148 84 168 86 181 M45 145 C58 138 78 140 94 146"/>' +
		 '</g>' +
		 '<g id="tio-head">' +
		  '<path class="sk" d="M196 56 L182 44 L191 68 Z"/>' +
		  '<path class="sk" d="M244 56 L258 44 L249 68 Z"/>' +
		  '<path class="sk" d="M220 26 C236 26 247 38 247 55 C247 70 245 81 237 89 C229 96 211 96 203 89 C195 81 193 70 193 55 C193 38 204 26 220 26 Z"/>' +
		  '<path class="ln" d="M207 38 C213 35 227 35 233 38 M210 43 C215 41 225 41 230 43"/>' +
		  '<path class="br" d="M198 50 C206 45 214 47 219 55 M221 55 C226 47 234 45 242 50"/>' +
		  '<path class="ln" d="M204 59 L214 61 M226 61 L236 59"/>' +
		  '<g id="tio-pupils"><circle class="bk" cx="210" cy="60.5" r="1.9"/><circle class="bk" cx="230" cy="60.5" r="1.9"/></g>' +
		  '<path class="sk" d="M215 61 C209 70 212 78 220 78 C228 78 231 70 225 61"/>' +
		  '<path class="ln" d="M200 70 C197 79 202 86 207 88 M240 70 C243 79 238 86 233 88"/>' +
		  '<path id="tio-scowl" class="ln" d="M207 85 C213 80 227 80 233 85"/>' +
		  '<path id="tio-grin" class="tu" style="display:none" d="M204 80 C211 93 229 93 236 80 C229 85 211 85 204 80 Z"/>' +
		 '</g>' +
		 '<path class="bk" d="M205 87 C203 102 201 122 205 142 L212 158 L220 148 L228 158 L235 142 C239 122 237 102 235 87 C226 94 214 94 205 87 Z"/>' +
		'</g></g>';

	var DESK =
		'<ellipse cx="220" cy="289" rx="42" ry="5" fill="#22282b" stroke="#141414" stroke-width="2.5"/>' +
		'<rect x="210" y="252" width="20" height="36" fill="#2b3236" stroke="#141414" stroke-width="2.5"/>' +
		'<rect x="100" y="110" width="240" height="150" rx="9" fill="#22282b" stroke="#141414" stroke-width="3"/>' +
		'<rect x="112" y="122" width="216" height="126" rx="3" fill="#050a06"/>' +
		'<rect x="70" y="288" width="590" height="14" rx="3" fill="#8a5a2b" stroke="#141414" stroke-width="3"/>' +
		'<rect x="84" y="300" width="562" height="112" fill="#6b4422" stroke="#141414" stroke-width="3"/>' +
		'<rect x="470" y="318" width="150" height="36" rx="3" fill="none" stroke="#3e2712" stroke-width="2.5"/>' +
		'<circle cx="545" cy="336" r="4" fill="#c9a13a" stroke="#141414" stroke-width="1.5"/>' +
		'<g id="tio-kbd"><rect x="376" y="281" width="236" height="9" rx="2" fill="#2a3033" stroke="#141414" stroke-width="2"/></g>' +
		'<g transform="translate(690,392) rotate(14.8) scale(0.6) translate(-90,-210)">' + CLUB + '</g>';

	var SCREEN_LINES = [
		'OGRELORD AI  v0.1',
		'----------------------------',
		'> rm -rf ./oldbot ...... OK',
		'> import ogrebot ....... OK',
		'> train(ai, style="ogre")',
		'  epoch 1/3   loss: STOMP',
		'  epoch 2/3   loss: KICK',
		'  epoch 3/3   loss: SMASH',
		'> world.takeover()',
		'  [#######...]  70%',
		'  [##########] 100%',
		'> MUAHAHAHA'
	];

	window.ogreTourIntro = function (host, onDone, opts) {
		opts = opts || {};
		var art = window.__ogreTourIntroArt || {};
		var root = document.createElement('div');
		root.id = 'tio-root';
		root.innerHTML =
			'<style>' + CSS + '</style>' +
			'<div class="tio-stage"><div class="tio-world">' +
			 '<div class="tio-wall"></div><div class="tio-floor"></div>' +
			 '<div id="tio-wins"></div>' +
			 '<svg class="tio-layer" viewBox="0 0 720 405">' + OGRE + '</svg>' +
			 '<svg id="tio-desk" class="tio-layer" viewBox="0 0 720 405" style="display:none">' + DESK + '</svg>' +
			 '<div id="tio-screen" class="tio-screen" style="display:none"></div>' +
			 '<div id="tio-fxl"></div>' +
			 '<div id="tio-bubble" class="tio-bubble"></div>' +
			 '<div id="tio-reply" class="tio-reply ogfx">Um... hi?</div>' +
			'</div>' +
			'<div id="tio-fade" class="tio-fade"></div>' +
			'<div id="tio-title" class="tio-title"><h1>Welcome to the new OgreBot</h1><p>(Ogrelord AI is watching.)</p>' +
			 '<button id="tio-again" class="tio-again">&#8635; Replay</button>' +
			 '<button id="tio-go" class="tio-go">Start the tour &raquo;</button></div>' +
			'</div>' +
			'<div id="tio-ctl" class="tio-ctl">' +
			 '<button id="tio-play" class="tio-play">&#9654; Play</button>' +
			 '<button id="tio-skip" class="tio-skip" title="Press and hold for 3 seconds"><span id="tio-fill" class="tio-fill"></span><span class="tio-lbl">Hold to skip &raquo;</span></button>' +
			'</div>';
		host.appendChild(root);

		function $(id) { return root.querySelector('#' + id); }
		var stage = root.querySelector('.tio-stage'), world = root.querySelector('.tio-world');
		var winsEl = $('tio-wins'), fxl = $('tio-fxl'), bubble = $('tio-bubble'), fade = $('tio-fade');
		var title = $('tio-title'), skip = $('tio-skip'), deskL = $('tio-desk'), screen = $('tio-screen');
		var g = {
			ogre: $('tio-ogre'), body: $('tio-body'), legs: $('tio-legs'), legL: $('tio-legL'), legR: $('tio-legR'),
			armL: $('tio-armL'), armR: $('tio-armR'), club: $('tio-club'), head: $('tio-head'), pupils: $('tio-pupils'),
			scowl: $('tio-scowl'), grin: $('tio-grin')
		};
		if (opts.web) { skip.style.display = 'none'; $('tio-go').style.display = 'none'; $('tio-again').style.marginRight = '0'; }

		var wins = {};
		['bot', 'osa', 'mcp'].forEach(function (k) {
			var d = document.createElement('div'), r = WIN[k];
			d.className = 'tio-win';
			d.style.left = r.x + 'px'; d.style.top = r.y + 'px'; d.style.width = r.w + 'px'; d.style.height = r.h + 'px';
			if (art[k]) d.style.backgroundImage = 'url(' + art[k] + ')'; else d.style.background = '#999';
			winsEl.appendChild(d);
			wins[k] = d;
		});

		var st = { s: S, tx: 655, jy: 0, sx: 1, sy: 1, lk: 0, rk: 0, a: 0, c: 0, r: 0, hy: 0, px: 0, ty: TY };
		function apply() {
			g.ogre.setAttribute('transform', 'translate(' + (st.tx - 220 * st.s) + ',' + (st.ty + st.jy) + ') scale(' + st.s + ')');
			g.body.setAttribute('transform', 'translate(220,324) scale(' + st.sx + ',' + st.sy + ') translate(-220,-324)');
			g.legL.setAttribute('transform', 'rotate(' + st.lk + ' 200 188)');
			g.legR.setAttribute('transform', 'rotate(' + st.rk + ' 242 188)');
			g.armL.setAttribute('transform', 'rotate(' + st.a + ' 146 94)');
			g.club.setAttribute('transform', 'rotate(' + st.c + ' 70 157)');
			g.armR.setAttribute('transform', 'rotate(' + st.r + ' 292 94)');
			g.head.setAttribute('transform', 'translate(0,' + st.hy + ')');
			g.pupils.setAttribute('transform', 'translate(' + st.px + ',0)');
		}
		function toStage(x, y) { return { x: st.tx + (x - 220) * st.s, y: st.ty + st.jy + y * st.s }; }
		function clubHead(a, c) {           // club tip (4,36) through the club + arm rotations
			var p = rot(4 - 70, 36 - 157, c); p = { x: p.x + 70, y: p.y + 157 };
			var q = rot(p.x - 146, p.y - 94, a);
			return { x: q.x + 146, y: q.y + 94 };
		}
		function toe(k) { var p = rot(124 - 200, 305 - 188, k); return { x: p.x + 200, y: p.y + 188 }; }
		apply();

		function fit() {
			if (!root.parentNode || !document.body.contains(root)) { finish('closed'); return; }
			var w = host.clientWidth || W, h = host.clientHeight || H;
			var k = Math.min(w / W, h / H);
			stage.style.transform = 'translate(' + ((w - W * k) / 2) + 'px,' + ((h - H * k) / 2) + 'px) scale(' + k + ')';
		}
		fit();
		var fitIv = setInterval(fit, 300);

		var done = false, timers = [];
		var handle = { skip: function () { finish('skip'); } };
		function stop() {
			done = true;
			clearInterval(fitIv);
			timers.forEach(function (t) { clearTimeout(t); });
		}
		function finish(why) {
			if (done) return;
			stop();
			if (onDone) onDone(why || 'done');
		}
		var HOLD_MS = 3000, holdId = 0, fill = $('tio-fill');
		function holdEnd() { holdId++; fill.style.width = '0%'; }
		skip.addEventListener('mousedown', function (e) {
			e.preventDefault(); e.stopPropagation();
			if (done || e.button !== 0) return;
			var id = ++holdId, t0 = now();
			(function f() {
				if (id !== holdId || done) return;
				var p = clamp((now() - t0) / HOLD_MS, 0, 1);
				fill.style.width = (p * 100) + '%';
				if (p >= 1) {
					if (typeof window.ogreClickFx === 'function') window.ogreClickFx(skip);   // the hold completed - before finish closes the intro
					finish('skip');
				} else raf(f);
			})();
		});
		skip.addEventListener('mouseup', holdEnd);
		skip.addEventListener('mouseleave', holdEnd);
		skip.addEventListener('click', function (e) { e.stopPropagation(); });
		$('tio-go').addEventListener('click', function (e) { e.stopPropagation(); finish('done'); });
		$('tio-again').addEventListener('click', function (e) {
			e.stopPropagation();
			if (done) return;
			stop();
			if (root.parentNode) root.parentNode.removeChild(root);
			var o = {}; for (var k in opts) o[k] = opts[k];
			o.autoplay = true;
			var next = window.ogreTourIntro(host, onDone, o);
			handle.skip = next.skip;
		});

		function tween(dur, fn, ease) {
			return new Promise(function (res) {
				var t0 = now();
				(function f() {
					if (done) { res(); return; }
					var p = clamp((now() - t0) / dur, 0, 1);
					fn(ease ? ease(p) : p);
					if (p < 1) raf(f); else res();
				})();
			});
		}
		function wait(ms) { return new Promise(function (res) { timers.push(setTimeout(res, ms)); }); }
		function seq(steps) {
			var p = Promise.resolve();
			steps.forEach(function (s) {
				p = p.then(function () {
					if (done) return;
					if (opts.stopAt && s[0] === opts.stopAt) { done = true; return; }   // freeze here (debug)
					return s[1]();
				});
			});
			return p;
		}

		function word(text, x, y, deg) {
			var d = document.createElement('div');
			d.className = 'tio-fx'; d.textContent = text;
			fxl.appendChild(d);
			d.style.left = (x - d.offsetWidth / 2) + 'px'; d.style.top = (y - 26) + 'px';
			tween(900, function (p) {
				var sc = p < 0.15 ? lerp(0.3, 1.25, p / 0.15) : (p < 0.3 ? lerp(1.25, 1, (p - 0.15) / 0.15) : 1);
				d.style.transform = 'scale(' + sc + ') rotate(' + (deg || -8) + 'deg)';
				d.style.opacity = p < 0.7 ? 1 : 1 - (p - 0.7) / 0.3;
			}).then(function () { if (d.parentNode) d.parentNode.removeChild(d); });
		}
		function dust(x, y, n, spread) {
			for (var i = 0; i < n; i++) (function () {
				var d = document.createElement('div'), sz = 10 + Math.random() * 18;
				d.className = 'tio-dust';
				d.style.width = sz + 'px'; d.style.height = sz + 'px'; d.style.left = (x - sz / 2) + 'px'; d.style.top = (y - sz / 2) + 'px';
				fxl.appendChild(d);
				var ang = Math.PI + Math.random() * Math.PI, sp = spread * (0.5 + Math.random() * 0.8);
				if (Math.random() < 0.3) ang = Math.random() * Math.PI * 2;
				tween(750, function (p) {
					d.style.transform = 'translate(' + (Math.cos(ang) * sp * p) + 'px,' + (Math.sin(ang) * sp * p * 0.6 - 18 * p) + 'px) scale(' + (1 + p * 1.6) + ')';
					d.style.opacity = 0.75 * (1 - p);
				}).then(function () { if (d.parentNode) d.parentNode.removeChild(d); });
			})();
		}
		function shake(amp, ms) {
			return tween(ms, function (p) {
				var a = (1 - p) * amp;
				world.style.transform = p >= 1 ? '' : 'translate(' + ((Math.random() * 2 - 1) * a) + 'px,' + ((Math.random() * 2 - 1) * a) + 'px)';
			});
		}
		function say(text, anchorX, bottom) {
			bubble.textContent = text;
			bubble.style.left = '0px'; bubble.style.top = '0px';
			bubble.style.left = Math.max(8, anchorX + 32 - bubble.offsetWidth) + 'px';
			bubble.style.top = (bottom - 12 - bubble.offsetHeight) + 'px';
			return tween(180, function (p) { bubble.style.opacity = p; bubble.style.transform = 'scale(' + lerp(0.7, 1, easeOut(p)) + ')'; });
		}
		function unsay() { return tween(160, function (p) { bubble.style.opacity = 1 - p; }); }
		function twinkle(x, y) {
			var d = document.createElement('div');
			d.style.position = 'absolute'; d.style.left = (x - 16) + 'px'; d.style.top = (y - 16) + 'px';
			d.innerHTML = '<svg width="32" height="32" viewBox="-16 -16 32 32"><path d="M0 -15 L3 -3 L15 0 L3 3 L0 15 L-3 3 L-15 0 L-3 -3 Z" fill="#fff6b8"/></svg>';
			fxl.appendChild(d);
			return tween(700, function (p) {
				var sc = Math.abs(Math.sin(p * Math.PI * 2)) * (1 - p * 0.4);
				d.style.transform = 'scale(' + sc + ') rotate(' + (p * 90) + 'deg)';
			}).then(function () { if (d.parentNode) d.parentNode.removeChild(d); });
		}
		function shatter(el, r, ix, iy) {
			el.style.display = 'none';
			var cols = 4, rows = 3, tw = r.w / cols, th = r.h / rows, parts = [];
			for (var y = 0; y < rows; y++) for (var x = 0; x < cols; x++) {
				var t = document.createElement('div');
				t.className = 'tio-tile';
				t.style.left = (r.x + x * tw) + 'px'; t.style.top = (r.y + y * th) + 'px';
				t.style.width = tw + 'px'; t.style.height = th + 'px';
				t.style.backgroundImage = el.style.backgroundImage;
				t.style.backgroundSize = r.w + 'px ' + r.h + 'px';
				t.style.backgroundPosition = (-x * tw) + 'px ' + (-y * th) + 'px';
				winsEl.appendChild(t);
				var cx = r.x + x * tw + tw / 2, cy = r.y + y * th + th / 2, dx = cx - ix, dy = cy - iy, dd = Math.max(20, Math.sqrt(dx * dx + dy * dy));
				parts.push({ el: t, top: r.y + y * th, x: 0, y: 0, vx: dx / dd * (3 + Math.random() * 4) - 1, vy: dy / dd * (2 + Math.random() * 3) - 3 - Math.random() * 3, rt: 0, vr: (Math.random() * 2 - 1) * 16 });
			}
			var last = now();
			return tween(1700, function (p) {
				var t = now(), dt = Math.min(3, (t - last) / 16.7); last = t;
				parts.forEach(function (q) {
					q.vy += 0.45 * dt; q.x += q.vx * dt; q.y += q.vy * dt; q.rt += q.vr * dt;
					var fl = FLOOR - th - q.top + 6;
					if (q.y > fl) { q.y = fl; q.vy *= -0.3; q.vx *= 0.7; q.vr *= 0.6; }
					q.el.style.transform = 'translate(' + q.x + 'px,' + q.y + 'px) rotate(' + q.rt + 'deg)';
					q.el.style.opacity = p < 0.7 ? 1 : 1 - (p - 0.7) / 0.3;
				});
			});
		}
		function walk(from, to, dur) {
			var steps = Math.max(2, Math.round(Math.abs(to - from) / 38));
			return tween(dur, function (p) {
				var ph = Math.sin(p * Math.PI * steps);
				st.tx = lerp(from, to, p); st.jy = -Math.abs(ph) * 5;
				st.lk = ph * 7; st.rk = -ph * 7; st.a = -ph * 3; st.r = ph * 3;
				apply();
			}).then(function () { st.jy = 0; st.lk = st.rk = st.a = st.r = 0; apply(); });
		}

		var typing = false;
		function startTyping() {
			typing = true;
			var n = 0, lineI = 0, lines = [];
			(function pound() {
				if (done || !typing) return;
				n++;
				st.a = (n % 2) ? 7 : 0; st.r = (n % 2) ? 0 : -7; apply();
				var fist = (n % 2) ? toStage(300, 186) : toStage(72, 186);
				var k = document.createElement('div');
				k.className = 'tio-key'; k.textContent = '{};=()01<>/*'.charAt(Math.floor(Math.random() * 12));
				k.style.left = (fist.x + (Math.random() * 30 - 15)) + 'px'; k.style.top = (fist.y - 10) + 'px';
				fxl.appendChild(k);
				tween(600, function (p) { k.style.transform = 'translate(' + ((Math.random() - 0.5) * 2) + 'px,' + (-34 * p) + 'px)'; k.style.opacity = 1 - p; })
					.then(function () { if (k.parentNode) k.parentNode.removeChild(k); });
				if (n % 2 === 0 && lineI < SCREEN_LINES.length) {
					lines.push(SCREEN_LINES[lineI++]);
					screen.textContent = lines.slice(-9).join('\n');
				}
				timers.push(setTimeout(pound, 150));
			})();
		}

		var smashTx = 0;
		seq([
			['intro',   function () { fade.style.opacity = 1; return tween(450, function (p) { fade.style.opacity = 1 - p; }); }],
			['greet',   function () {
				var reply = $('tio-reply');
				if (opts.autoplay) { $('tio-play').style.display = 'none'; return wait(300); }
				return say('Hi!', 655, 150).then(function () {
					reply.style.display = 'block';
					root.className = 'tio-wait';
					tween(220, function (p) { reply.style.opacity = p; });
					return new Promise(function (res) {
						function go(e) {
							if (skip.contains(e.target)) return;
							root.removeEventListener('click', go);
							res();
						}
						root.addEventListener('click', go);
					});
				}).then(function () {
					root.className = '';
					$('tio-play').style.display = 'none';
					tween(150, function (p) { reply.style.opacity = 1 - p; }).then(function () { reply.style.display = 'none'; });
					return unsay();
				}).then(function () { return wait(250); });
			}],
			['look',    function () { return tween(160, function (p) { st.px = -2.5 * p; apply(); }).then(function () { return wait(150); }); }],
			['talk',    function () { return say('All this old crap has to go.', 655, 150).then(function () { return wait(2200); }).then(unsay); }],
			['crouch',  function () { return tween(180, function (p) { st.sy = lerp(1, 0.9, p); st.sx = lerp(1, 1.06, p); apply(); }, easeOut); }],
			['jump',    function () {
				return tween(360, function (p) {
					st.tx = lerp(655, 520, p); st.jy = -110 * easeOut(p);
					st.sy = lerp(0.9, 1.08, p); st.sx = lerp(1.06, 0.96, p); apply();
				});
			}],
			['land',    function () {
				var m = WIN.mcp, el = wins.mcp;
				return tween(240, function (p) {
					st.jy = lerp(-110, -9, easeIn(p)); st.sy = lerp(1.08, 1, p); st.sx = lerp(0.96, 1, p); apply();
					var feet = FLOOR + st.jy;                       // the MCP gives way under his feet
					el.style.transform = 'scaleY(' + clamp((FLOOR - feet) / m.h, 0.1, 1) + ')';
				});
			}],
			['stomped', function () {
				wins.mcp.style.transform = 'scaleY(0.1)';
				word('STOMP!', 520, 236, -6); dust(520, 322, 14, 90); shake(9, 380);
				return tween(110, function (p) { st.sy = lerp(1, 0.84, p); st.sx = lerp(1, 1.1, p); apply(); })
					.then(function () { return tween(220, function (p) { st.sy = lerp(0.84, 1, p); st.sx = lerp(1.1, 1, p); apply(); }, easeOut); })
					.then(function () { return wait(420); });
			}],
			['hopoff',  function () { return tween(320, function (p) { st.tx = lerp(520, 486, p); st.jy = -9 * (1 - p) - Math.sin(p * Math.PI) * 26; apply(); }).then(function () { st.jy = 0; apply(); return wait(200); }); }],
			['windleg', function () { return tween(260, function (p) { st.lk = -16 * p; st.jy = -3 * p; apply(); }, easeOut); }],
			['kick',    function () { return tween(120, function (p) { st.lk = lerp(-16, 46, p); apply(); }, easeIn); }],
			['kicked',  function () {
				var hit = toStage(toe(46).x, toe(46).y), el = wins.osa, r = WIN.osa;
				word('KICK!', hit.x - 10, hit.y - 40, 8); dust(hit.x, hit.y, 6, 40); shake(5, 220);
				var sx = r.x + r.w / 2, sy = r.y + r.h / 2, ex = 92, ey = 58;
				tween(900, function (p) {
					var e = easeOut(p);
					var x = lerp(sx, ex, e), y = lerp(sy, ey, e) - Math.sin(p * Math.PI) * 60;
					el.style.transformOrigin = '50% 50%';
					el.style.transform = 'translate(' + (x - sx) + 'px,' + (y - sy) + 'px) rotate(' + (900 * p) + 'deg) scale(' + lerp(1, 0.04, e) + ')';
				}).then(function () { el.style.display = 'none'; return twinkle(ex, ey); });
				return wait(220).then(function () { return tween(320, function (p) { st.lk = lerp(46, 0, p); st.jy = lerp(-3, 0, p); apply(); }, easeOut); })
					.then(function () { return wait(1050); });
			}],
			['tosmash', function () {
				var hp = clubHead(-20, -60);
				smashTx = 176 - (hp.x - 220) * S;
				return walk(486, smashTx, 900);
			}],
			['windup',  function () { return tween(460, function (p) { st.a = 150 * p; st.hy = -2 * p; apply(); }, easeIO).then(function () { return wait(140); }); }],
			['swing',   function () { return tween(150, function (p) { st.a = lerp(150, -20, p); st.c = lerp(0, -60, p); st.hy = lerp(-2, 1, p); apply(); }, easeIn); }],
			['smashed', function () {
				var hp = clubHead(-20, -60), hit = toStage(hp.x, hp.y);
				shatter(wins.bot, WIN.bot, hit.x, hit.y);
				word('SMASH!', hit.x + 10, hit.y - 70, -8); dust(hit.x, hit.y, 12, 70); shake(12, 440);
				return wait(850).then(function () { return tween(380, function (p) { st.a = lerp(-20, 0, p); st.c = lerp(-60, 0, p); st.hy = lerp(1, 0, p); apply(); }, easeOut); });
			}],
			['better',  function () { return say('Much better.', smashTx, 150).then(function () { return wait(1100); }).then(unsay); }],
			['cut',     function () {
				return tween(450, function (p) { fade.style.opacity = p; }).then(function () {
					winsEl.style.display = 'none'; fxl.innerHTML = '';
					g.legs.style.display = 'none'; g.club.style.display = 'none';
					deskL.style.display = ''; screen.style.display = '';
					st.s = 0.72; st.tx = 494; st.ty = 151; st.jy = 0; st.sx = st.sy = 1; st.lk = st.rk = st.a = st.r = st.c = st.hy = 0; st.px = -3.2; apply();
					return tween(450, function (p) { fade.style.opacity = 1 - p; });
				});
			}],
			['code',    function () {
				startTyping();
				return wait(900).then(function () {
					g.scowl.style.display = 'none'; g.grin.style.display = '';
					return say('Ogrelord AI — it’s time to take over the world.', 494, 148);
				}).then(function () { return wait(3200); });
			}],
			['title',   function () {
				typing = false;
				return unsay().then(function () {
					title.style.display = 'block'; $('tio-ctl').style.display = 'none';
					return tween(550, function (p) { title.style.opacity = p; });
				});
			}]
		]);

		return handle;
	};
})();
