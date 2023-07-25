var SceneOne = new Phaser.Class({
    Extends: Phaser.Scene,
    initialize: function() {
        Phaser.Scene.call(this, {"key": "SceneOne" });
    },



    preload: function()
    {
        //this.load.image('village', 'assets/backgrounds/village.png');
        this.load.image('background1', 'assets/backgrounds/GRADIENT1.jpg')
        
        this.load.image('base_tiles', 'assets/tilesets/OutDoorsTileset.png');
        this.load.tilemapTiledJSON('tilemap','assets/MAP.json');
        
        this.load.audio('outdoormusic', "assets/music/outdoortheme.wav");

        // protagonist load in
        this.load.spritesheet('inukWalkRight', 
            'assets/sprite/inukWalkRight.png',
            { frameWidth: 51.5, frameHeight: 80});
        this.load.spritesheet('inukWalkLeft', 
            'assets/sprite/inukWalkLeft.png',
            { frameWidth: 51.5, frameHeight: 80});
        this.load.spritesheet('inukIdle', 
            'assets/sprite/inukIdle.png',
            { frameWidth: 51.5, frameHeight: 77});
        
        this.load.spritesheet('inukShootLeft', 
            'assets/sprite/inukShootLeft.png',
            { frameWidth: 66.67, frameHeight: 80});
        this.load.spritesheet('inukShootRight', 
            'assets/sprite/inukShootRight.png',
            { frameWidth: 66.67, frameHeight: 80});
        this.load.spritesheet('inukDeath', 
            'assets/sprite/inukDeath.png',
            { frameWidth: 58.26, frameHeight: 80});


        this.load.image('arrow', 'assets/arrow.png');

        // snow golem load in
        this.load.spritesheet('snowGolem', 
        'assets/enemies/snowGolem.png',
        { frameWidth: 44, frameHeight: 60});

        this.load.image('floor', 'assets/floor.png');
    },
    
    create: function()
    {
        
        this.add.image(0, 0, 'base_tiles')
        this.add.image(400, 1600, 'background1')
        
        map = this.make.tilemap({key: 'tilemap'});
        const tileset = map.addTilesetImage('snowleveltileset','base_tiles');
        //const layer = map.createLayer("toplayer", tileset, 0, 0);
        
        
        //map.createLayer('sky', tileset)
        const platforms = map.createLayer('platforms', tileset)
        map.createLayer('aesthetics', tileset)
        
        
        
        platforms.setCollisionByProperty({ collides: 'yes'})
        
        outdoormusic = this.sound.add('outdoormusic', {volume: 0.15}, {loop: true});
        outdoormusic.play();
        
        cursors = this.input.keyboard.createCursorKeys();
        //this.add.image(400, 400, 'village');
        
        // floor
        //floor = this.physics.add.staticGroup();
        //floor.create(400, 800, 'floor');

        // score 
        score = 0;
        scoreText = this.add.text(16, 16, 'Points: ' + score, { fontSize: '24px', fill: '#000' });
        scoreText.setBackgroundColor('white')

        // health bar
        sceneHealth = 100;
        bar = this.add.graphics();
        healthBar = makeBar(550, 16, 0x03fc03, bar);
        setValue(healthBar, 100);
        function makeBar(x, y, color, bar)
        {
            bar = bar;
            bar.fillStyle(color, 1);
            bar.fillRect(0, 0, 200, 30);
            bar.x = x;
            bar.y = y;
            return bar;
        }

        function setValue(bar, percent)
        {
            bar.scaleX = percent / 100;
        }

        // player
        this.cameras.main.centerOn(400, 2800);
        player = this.physics.add.sprite(100, 3000, 'inukWalkRight');
        player.setBounce(0);
        
        this.physics.world.setBounds(0, 0, 800, 3200, true, true, true, true);
        player.setCollideWorldBounds(true);
        this.physics.add.collider(player, platforms);
        
        this.cameras.main.setBounds(0, 0, 800, 3200);
        this.cameras.main.startFollow(player);

        // scene specific asset creation
        snowGolems = this.physics.add.group({ key: 'snowGolem', allowGravity: false });
        arrows = this.physics.add.group( { allowGravity: false });

        
        // arrow and enemy colliders
        //this.physics.add.collider(arrows, snowGolems, arrSG, null, this);
    

        // enemy and floor colliders
        this.physics.add.collider(arrows, snowGolems, arrSG, null, this);
        function arrSG(arrow, snowGolem)
        {
            snowGolem.disableBody(true, true);
            arrow.disableBody(true, true);
            score += 10;
            scoreText.setText('Points: ' + score);
        }
        
        function floSG(snowGolem)
        {
            snowGolem.disableBody(true, true);
            if (score >= 20)
            {
                score -= 20;
                scoreText.setText('Points: ' + score);
            }
        }

        // ememy and player colliders
        this.physics.add.collider(snowGolems, player, playerSG, null, this);
        function playerSG(player, snowGolem)
        {
            sceneHealth = sceneHealth - 20;
            snowGolem.disableBody(true, true);
            outdoormusic.stop();
            //this.scene.stop('SceneOne');
            map.destroy();
            this.scene.start('SceneZero');
        }

        //player animations
        this.anims.create({
            key: 'left',
            frames: this.anims.generateFrameNumbers('inukWalkLeft', { start: 0, end: 4}),
            frameRate: 10,
            repeat: -1
        });

        this.anims.create({
            key: 'right',
            frames: this.anims.generateFrameNumbers('inukWalkRight', { start: 0, end: 4}),
            frameRate: 10,
            repeat: -1
        });

        this.anims.create({
            key: 'turnright',
            frames: [ { key: 'inukIdle', frame: 1 } ],
            frameRate: 20
        });

        this.anims.create({
            key: 'turnleft',
            frames: [ { key: 'inukIdle', frame: 0 } ],
            frameRate: 20
        });

        this.anims.create({
            key: 'shootLeft',
            frames: [ { key: 'inukShootLeft', frame: 0 } ],
            frameRate: 30,
            repeat: -1
        })

        this.anims.create({
            key: 'shootRight',
            frames: [ { key: 'inukShootRight', frame: 0 } ],
            frameRate: 30,
            repeat: -1
        })

        this.anims.create({
            key: 'death',
            frames: this.anims.generateFrameNumbers('inukDeath', { start: 0, end: 7}),
            frameRate: 5,
            repeat: -1
        });

        //enemy animation
        this.anims.create({
            key: 'snowGolem',
            frames: this.anims.generateFrameNumbers('snowGolem', { start: 0, end: 7}),
            frameRate: 10,
            repeat: -1
        });

    },
    
    update: function()
    {
        
        if (player.body.blocked.down)
            {
                hasJump = 1
            }
        // player movement
        if (cursors.left.isDown)
        {   

            direction = "left"
            attacking = false
            player.setVelocityX(-400);
            player.anims.play('left', true);
    
        }
        else if (cursors.right.isDown)
        {
            direction = "right"
            attacking = false
            player.setVelocityX(400);
            player.anims.play('right', true);
        
        }
        else 
        {
            attacking = false
            if (direction == 'right')
            {
                player.anims.play('turnright');
            }
            if (direction == 'left') 
            {
                player.anims.play('turnleft');
            }
            player.setVelocityX(0);

        }

        if (cursors.up.isDown && hasJump == 1)
        { 
            // jump 
            player.setVelocityY(-850);
            hasJump = 0;
        }

        if (cursors.space.isDown && arrowTimer > this.time.now)
        {
            if (direction == 'right')
            {
                player.anims.play('shootRight');
            }
            if (direction == 'left') 
            {
                player.anims.play('shootLeft');
            }

        }

        if (cursors.space.isDown && arrowTimer < this.time.now)
        {

            attacking = true
            if (direction == 'right')
            {
                player.anims.play('shootRight');
            }
            if (direction == 'left') 
            {
                player.anims.play('shootLeft');
            }

            arrow = arrows.create(player.x, player.y - 80,'arrow');
            arrow.setVelocityY(-750);
            arrowTimer = this.time.now + 250;

        }



        // enemy creation
        if (this.time.now > cocoTimer)
        {

            xCoor = Phaser.Math.Between(50, 750);
            snowGolem = snowGolems.create(xCoor, 0, 'snowGolem');
            snowGolem.anims.play('snowGolem');
            snowGolem.setVelocityY(150);
            cocoTimer = this.time.now + 2700;

        }

        // score and scene change
        //if (score == 30)
        //{   
        //    outdoormusic.stop();
        //    this.scene.stop('SceneOne');
        //    this.scene.start('SceneTwo');
        //}

        // player death
        if (sceneHealth == 0)
        {
            player.anims.play('death');
            player.setVelocityX(0);
            snowGolems.setVelocityY(0);
            outdoormusic.stop();
            //this.scene.stop('SceneOne');
            map.destroy();
            this.scene.start('SceneZero');

            
        }
        
        if (player.x > 640 && player.y < 640)
        {
            outdoormusic.stop();
            map.destroy();
            this.scene.start('SceneTwo'); 
        }
        
        //if (player.y == 721 && hasJump == 1)
            //this.scene.stop('SceneOne');
            //this.scene.start('SceneTwo');
        



    }, 

});