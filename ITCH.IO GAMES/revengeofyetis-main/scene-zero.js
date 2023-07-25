var SceneZero = new Phaser.Class({
    Extends: Phaser.Scene,
    initialize: function() {
        Phaser.Scene.call(this, {"key": "SceneZero" });
    },

                            
    preload: function()
    {
        this.load.image('title', 'assets/backgrounds/titlescreennoback.png');
        this.load.audio('titlemusic', "assets/music/titlemusic.wav");
        
        this.load.image('sky', 'assets/snowyMountain/Above_sky.png')
        this.load.image('clouds', 'assets/snowyMountain/Above_clouds.png')
        this.load.image('smallmountains', 'assets/snowyMountain/Above_MTN_back.png')
        this.load.image('bigmountains', 'assets/snowyMountain/Above_MTN.png')
        this.load.image('smalltrees', 'assets/snowyMountain/Above_Trees.png')
        this.load.image('bigtrees', 'assets/snowyMountain/Above_TreesBig.png')
        
        this.load.spritesheet('inukWalkRight', 
            'assets/sprite/inukWalkRight.png',
            { frameWidth: 51.5, frameHeight: 79});
    },
    
    create: function()
        
    {   
        const createAligned = (scene, count, texture, scrollFactor, h, sc) => {
            let x = scene.scale.width * 0.5
            
            for (let i = 0; i < count; ++ i)
            {
                const y = scene.add.image(x, h, texture).setScale(sc)
                    .setScrollFactor(scrollFactor)

                x += y.width * 1.25
            }
    
        }
        

        titlemusic = this.sound.add('titlemusic', {volume: 0.15});
        titlemusic.loop = true;
        titlemusic.play();
    
        cursors = this.input.keyboard.createCursorKeys();
        
        const width = this.scale.width
        const height = this.scale.height
        
        this.add.image(400, 400, 'sky').setScale(1.25)
            .setScrollFactor(0)

        createAligned(this, 4, 'clouds', 0.25 *0.5, 400, 1.25)
        createAligned(this, 6, 'smallmountains', 0.375 *0.5, 400, 1.25)
        createAligned(this, 10, 'bigmountains', 0.5 *0.5, 400, 1.25)
        createAligned(this, 15, 'smalltrees', 1 *0.5, 400, 1.25)
        createAligned(this, 15, 'smalltrees', 1.125 *0.5, 450, 1.25)
        createAligned(this, 15, 'bigtrees', 1.25 *0.5, 400, 1.25)
        createAligned(this, 15, 'bigtrees', 1.375 *0.5, 475, 1.25)
        
        
        var player = this.physics.add.sprite(400, 760, 'inukWalkRight');
        this.physics.world.setBounds(0, 0, 8000, 800, true, true, true, true);
        player.setCollideWorldBounds(true);
        
        this.anims.create({
            key: 'right',
            frames: this.anims.generateFrameNumbers('inukWalkRight', { start: 5, end: 0}),
            frameRate: 5,
            repeat: -1
        });
        
        player.setVelocityX(50);
        player.anims.play('right', true); 
        
        this.cameras.main.setBounds(0, 0, width * 10, 800);
        
        this.cameras.main.startFollow(player);
        
        this.add.image(400, 400, 'title').setScale(4/3)
            .setScrollFactor(0)
    },
    
    update: function()
    {
        //if (player.x > 2800)
        //{
            //player.x = 400
        //}
        if (cursors.space.isDown)
        {   
            titlemusic.stop();
            this.scene.stop('SceneZero');
            this.scene.start('SceneOne');
        }
    }
});