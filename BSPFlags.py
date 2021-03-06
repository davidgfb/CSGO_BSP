MAX_BRUSH_LIGHTMAP_DIM_WITHOUT_BORDER   = 32
MAX_BRUSH_LIGHTMAP_DIM_INCLUDING_BORDER = 35
MAX_DISP_LIGHTMAP_DIM_WITHOUT_BORDER    = MAX_LIGHTMAP_DIM_WITHOUT_BORDER   = 128
MAX_DISP_LIGHTMAP_DIM_INCLUDING_BORDER  = MAX_LIGHTMAP_DIM_INCLUDING_BORDER = 131

DIST_EPSILON              = 0.03125
MAX_SURFINFO_VERTS        = 32
BSPVERSION                = 19
HEADER_LUMPS              = 64

MAX_POLYGONS              = 50120
MAX_MOD_KNOWN             = 512
MAX_MAP_MODELS            = 1024
MAX_MAP_BRUSHES           = 8192
MAX_MAP_ENTITIES          = 4096
MAX_MAP_ENTSTRING         = 262144
MAX_MAP_NODES             = 65536
MAX_MAP_TEXINFO           = 12288
MAX_MAP_TEXDATA           = 2048
MAX_MAP_LEAFBRUSHES       = 65536

MIN_MAP_DISP_POWER        = 2

MAX_MAP_DISP_POWER        = 4
MAX_MAP_SURFEDGES         = 512000
MAX_DISP_CORNER_NEIGHBORS = 4

SURF_LIGHT     = 0x0001 # value will hold the light strength
SURF_SLICK     = 0x0002 # effects game physics
SURF_SKY       = 0x0004 # don't draw, but add to skybox
SURF_WARP      = 0x0008 # turbulent water warp
SURF_TRANS     = 0x0010
SURF_WET       = 0x0020 # the surface is wet
SURF_FLOWING   = 0x0040 # scroll towards angle
SURF_NODRAW    = 0x0080 # don't bother referencing the texture
SURF_Hint32_t  = 0x0100 # make a primary bsp splitter
SURF_SKIP      = 0x0200 # completely ignore, allowing non-closed brushes
SURF_NOLIGHT   = 0x0400 # Don't calculate light
SURF_BUMPLIGHT = 0x0800 # calculate three lightmaps for the surface for bumpmapping
SURF_HITBOX    = 0x8000 # surface is part of a hitbox

CONTENTS_EMPTY         = 0           # No contents
CONTENTS_SOLID         = 0x1         # an eye is never valid in a solid
CONTENTS_WINDOW        = 0x2         # translucent, but not watery (glass)
CONTENTS_AUX           = 0x4
CONTENTS_GRATE         = 0x8         # alpha-tested "grate" textures.  Bullets/sight pass through, but solids don't
CONTENTS_SLIME         = 0x10
CONTENTS_WATER         = 0x20
CONTENTS_MIST          = 0x40
CONTENTS_OPAQUE        = 0x80        # things that cannot be seen through (may be non-solid though)

LAST_VISIBLE_CONTENTS  = 0x80
ALL_VISIBLE_CONTENTS   = LAST_VISIBLE_CONTENTS | LAST_VISIBLE_CONTENTS - 1

CONTENTS_TESTFOGVOLUME = 0x100
CONTENTS_UNUSED3       = 0x200
CONTENTS_UNUSED4       = 0x400
CONTENTS_UNUSED5       = 0x800
CONTENTS_UNUSED6       = 0x1000
CONTENTS_UNUSED7       = 0x2000
CONTENTS_MOVEABLE      = 0x4000      # hits entities which are MOVETYPE_PUSH (doors, plats, etc.)

# remaining contents are non-visible, and don't eat brushes
CONTENTS_AREAPORTAL    = 0x8000
CONTENTS_PLAYERCLIP    = 0x10000
CONTENTS_MONSTERCLIP   = 0x20000

# currents can be added to any other contents, and may be mixed
CONTENTS_CURRENT_0     = 0x40000
CONTENTS_CURRENT_90    = 0x80000
CONTENTS_CURRENT_180   = 0x100000
CONTENTS_CURRENT_270   = 0x200000
CONTENTS_CURRENT_UP    = 0x400000
CONTENTS_CURRENT_DOWN  = 0x800000
CONTENTS_ORIGIN        = 0x1000000   # removed before bsping an entity
CONTENTS_MONSTER       = 0x2000000   # should never be on a brush, only in game
CONTENTS_DEBRIS        = 0x4000000
CONTENTS_DETAIL        = 0x8000000   # brushes to be added after vis leafs
CONTENTS_TRANSLUCENT   = 0x10000000  # int32_t set if any surface has trans
CONTENTS_LADDER        = 0x20000000
CONTENTS_HITBOX        = 0x40000000  # use accurate hitboxes on trace

# everyhting
MASK_ALL                   = 0xFFFFFFFF

# everything that is normally solid
MASK_SOLID                 = CONTENTS_SOLID | CONTENTS_MOVEABLE | CONTENTS_WINDOW | CONTENTS_MONSTER | CONTENTS_GRATE

# everything that blocks player movement
MASK_PLAYERSOLID           = CONTENTS_SOLID | CONTENTS_MOVEABLE | CONTENTS_PLAYERCLIP | CONTENTS_WINDOW | CONTENTS_MONSTER | \
                             CONTENTS_GRATE

# blocks npc movement
MASK_NPCSOLID              = CONTENTS_SOLID | CONTENTS_MOVEABLE | CONTENTS_MONSTERCLIP | CONTENTS_WINDOW | CONTENTS_MONSTER | \
                             CONTENTS_GRATE

# water physics in these contents
MASK_WATER                 = CONTENTS_WATER | CONTENTS_MOVEABLE | CONTENTS_SLIME

# everything that blocks line of sight
MASK_OPAQUE                = CONTENTS_SOLID | CONTENTS_MOVEABLE | CONTENTS_SLIME | CONTENTS_OPAQUE

# bullets see these as solid
MASK_SHOT                  = CONTENTS_SOLID | CONTENTS_MOVEABLE | CONTENTS_MONSTER | CONTENTS_WINDOW | CONTENTS_DEBRIS | \
                             CONTENTS_HITBOX

# non-raycasted weapons see this as solid (includes grates)
MASK_SHOT_HULL             = CONTENTS_SOLID | CONTENTS_MOVEABLE | CONTENTS_MONSTER | CONTENTS_WINDOW | CONTENTS_DEBRIS | \
                             CONTENTS_GRATE

# everything normally solid, except monsters (world+brush only)
MASK_SOLID_BRUSHONLY       = CONTENTS_SOLID | CONTENTS_MOVEABLE | CONTENTS_WINDOW | CONTENTS_GRATE

# everything normally solid for player movement, except monsters (world+brush only)
MASK_PLAYERSOLID_BRUSHONLY = CONTENTS_SOLID | CONTENTS_MOVEABLE | CONTENTS_WINDOW | CONTENTS_PLAYERCLIP | CONTENTS_GRATE

# everything normally solid for npc movement, except monsters (world+brush only)
MASK_NPCSOLID_BRUSHONLY    = CONTENTS_SOLID | CONTENTS_MOVEABLE | CONTENTS_WINDOW | CONTENTS_MONSTERCLIP | CONTENTS_GRATE

# just the world, used for route rebuilding
MASK_NPCWORLDSTATIC        = CONTENTS_SOLID | CONTENTS_WINDOW | CONTENTS_MONSTERCLIP | CONTENTS_GRATE

# UNDONE: This is untested, any moving water
MASK_CURRENT               = CONTENTS_CURRENT_0 | CONTENTS_CURRENT_90 | CONTENTS_CURRENT_180 | CONTENTS_CURRENT_270 | \
                             CONTENTS_CURRENT_UP | CONTENTS_CURRENT_DOWN
MASK_DEADSOLID             = CONTENTS_SOLID | CONTENTS_PLAYERCLIP | CONTENTS_WINDOW | CONTENTS_GRATE
