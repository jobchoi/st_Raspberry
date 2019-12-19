#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/types.h>
#include <linux/spi/spidev.h>


#define ARRAY_SIZE(a) (sizeof(a) / sizeof((a)[0]))
#define TWINKLE_LOOP 15

#define   RED   0x00ff0000  // »¡°­
#define   GREEN   0x0000ff00  // ³ì»ö
#define   BLUE    0x000000ff  // ÆÄ¶û
#define   YELLOW    0x00ffff00  // ³ë¶û
#define   SKYBLUE   0x0073d1f7  // ÇÏ´Ã»ö
#define   PINK    0x00f69fa8  // ºÐÈ«
#define   BLACK   0x00000000  // °ËÁ¤(OFF)
#define   BROWN   0x0088563f  // °¥»ö
#define   ORANGE  0x00f3753a  // ¿À·»Áö»ö
#define   DEEPBLUE  0x002a365c  // ³²»ö

static void pabort(const char *s)
{
  perror(s);
  abort();
}

static const char *device = "/dev/spidev0.0";
static uint8_t mode;
static uint8_t bits = 8;
static uint32_t speed = 2500000;//500000;
static uint16_t delay_1;

int byte_index = 0;
uint8_t* spread_msg;
uint8_t* rx;
uint16_t NUMPIXELS;


struct {
  uint8_t num;
  uint8_t* r;
  uint8_t* g;
  uint8_t* b;
  uint16_t* from;
  uint16_t* to;
  uint16_t* wait;
  uint16_t* run_time;
  uint16_t* func_num;
}f;

struct {
  //volatile uint8_t* tx;
  uint8_t* tx;
  int fd;
  void(*show)();
  void(*setPixelColor)(uint16_t n, uint32_t rgb);
  long (*Color)(uint8_t r, uint8_t g, uint8_t b);
}pixels;

static void transfer()
{
  int ret;
  
  struct spi_ioc_transfer tr = {
    .tx_buf = (unsigned long)spread_msg,
    .rx_buf = (unsigned long)rx,
    .len = NUMPIXELS * 3 * 3,
    //.delay_usecs = delay,
    .speed_hz = speed,
    .bits_per_word = bits,
  };
  spread_spi_bits(0, pixels.tx, NUMPIXELS);

  ret = ioctl(pixels.fd, SPI_IOC_MESSAGE(1), &tr);
  if (ret < 1)
    pabort("can't send spi message");

  for (ret = 0; ret < ARRAY_SIZE(pixels.tx); ret++) {
    //if (!(ret % 6))
      //puts("");
    //printf("%.2X ", rx[ret]);
  }
  //puts("");
  
}

static void print_usage(const char *prog)
{
  //printf("Usage: %s [-DsbdlHOLC3]\n", prog);
  puts("  -D --device   device to use (default /dev/spidev1.1)\n"
       "  -s --speed    max speed (Hz)\n"
       "  -d --delay    delay (usec)\n"
       "  -b --bpw      bits per word \n"
       "  -l --loop     loopback\n"
       "  -H --cpha     clock phase\n"
       "  -O --cpol     clock polarity\n"
       "  -L --lsb      least significant bit first\n"
       "  -C --cs-high  chip select active high\n"
       "  -3 --3wire    SI/SO signals shared\n");
  exit(1);
}

static void parse_opts(int argc, char *argv[])
{
  while (1) {
    static const struct option lopts[] = {
      { "device",  1, 0, 'D' },
      { "speed",   1, 0, 's' },
      { "delay",   1, 0, 'd' },
      { "bpw",     1, 0, 'b' },
      { "loop",    0, 0, 'l' },
      { "cpha",    0, 0, 'H' },
      { "cpol",    0, 0, 'O' },
      { "lsb",     0, 0, 'L' },
      { "cs-high", 0, 0, 'C' },
      { "3wire",   0, 0, '3' },
      { "no-cs",   0, 0, 'N' },
      { "ready",   0, 0, 'R' },
      { NULL, 0, 0, 0 },
    };
    int c;

    c = getopt_long(argc, argv, "D:s:d:b:lHOLC3NR", lopts, NULL);

    if (c == -1)
      break;

    switch (c) {
    case 'D':
      device = optarg;
      break;
    case 's':
      speed = atoi(optarg);
      break;
    case 'd':
      //delay = atoi(optarg);
      break;
    case 'b':
      bits = atoi(optarg);
      break;
    case 'l':
      mode |= SPI_LOOP;
      break;
    case 'H':
      mode |= SPI_CPHA;
      break;
    case 'O':
      mode |= SPI_CPOL;
      break;
    case 'L':
      mode |= SPI_LSB_FIRST;
      break;
    case 'C':
      mode |= SPI_CS_HIGH;
      break;
    case '3':
      mode |= SPI_3WIRE;
      break;
    case 'N':
      mode |= SPI_NO_CS;
      break;
    case 'R':
      mode |= SPI_READY;
      break;
    default:
      print_usage(argv[0]);
      break;
    }
  }
}

void delay(uint16_t wait)
{
  usleep(wait*1000);
}
long setColor(uint8_t r, uint8_t g, uint8_t b);
void PixelColor(uint16_t n, uint32_t rgb);
void spread_spi_bits(uint8_t start, uint8_t *msg, uint16_t led_num);
void Led(uint16_t from,uint16_t to,uint16_t wait,uint8_t r,uint8_t g,uint8_t b);
void sel_func(uint16_t NUMPIXELS);
void run_func();

int main(int argc, char *argv[])
{
  pixels.show = transfer;
  pixels.setPixelColor = PixelColor;
  pixels.Color = setColor;
  parse_opts(argc, argv);
  int ret = 0;
  pixels.fd = open(device, O_RDWR);

  if (pixels.fd < 0)
    pabort("can't open device");

  /*
   * spi mode
   */
  ret = ioctl(pixels.fd, SPI_IOC_WR_MODE, &mode);
  if (ret == -1)
    pabort("can't set spi mode");

  ret = ioctl(pixels.fd, SPI_IOC_RD_MODE, &mode);
  if (ret == -1)
    pabort("can't get spi mode");

  /*
   * bits per word
   */
  ret = ioctl(pixels.fd, SPI_IOC_WR_BITS_PER_WORD, &bits);
  if (ret == -1)
    pabort("can't set bits per word");

  ret = ioctl(pixels.fd, SPI_IOC_RD_BITS_PER_WORD, &bits);
  if (ret == -1)
    pabort("can't get bits per word");

  /*
   * max speed hz
   */
  ret = ioctl(pixels.fd, SPI_IOC_WR_MAX_SPEED_HZ, &speed);
  if (ret == -1)
    pabort("can't set max speed hz");

  ret = ioctl(pixels.fd, SPI_IOC_RD_MAX_SPEED_HZ, &speed);
  if (ret == -1)
    pabort("can't get max speed hz");

  NUMPIXELS = 16; // LED(H/W) : 12 -> sw상에서 입력값을 16으로해야정상적으로 제어됨 8진수에서 16은 20으로
  printf("number of Controll led : %d\n", NUMPIXELS);

  pixels.tx = (uint8_t*)malloc(sizeof(uint8_t)*(NUMPIXELS*3));
  rx = (uint8_t*)malloc(sizeof(uint8_t)*(NUMPIXELS * 3 * 3));
  spread_msg = (uint8_t*)malloc(sizeof(uint8_t)*(NUMPIXELS * 3 * 3));

  int i = 0;

  while(i < 1){
	  sel_func(NUMPIXELS);
	  i++;
  }
  close(pixels.fd);

 // return ret;
}

long setColor(uint8_t r, uint8_t g, uint8_t b)
{
  static uint32_t rgb = {0};
  rgb = ((r<<20)|(r<<16))|((g<<12)|(g<<8))|((b<<4)|b);
  return rgb;
}

void sel_func(uint16_t NUMPIXELS)
{
    uint8_t i = 0;
    printf("\n");
    printf("================== [WS2812 LED TEST] ==================\n");
    printf("        [1] LED ON \n");
    printf("=======================================================\n");
    printf("\n");

	f.num = 1;

    printf("\n");
    f.func_num = (uint16_t*)malloc(sizeof(uint16_t)*(f.num));
    f.r = (uint8_t*)malloc(sizeof(uint8_t)*(f.num));
    f.g = (uint8_t*)malloc(sizeof(uint8_t)*(f.num));
    f.b = (uint8_t*)malloc(sizeof(uint8_t)*(f.num));
    f.from = (uint16_t*)malloc(sizeof(uint16_t)*(f.num));
    f.to = (uint16_t*)malloc(sizeof(uint16_t)*(f.num));
    f.wait = (uint16_t*)malloc(sizeof(uint16_t)*(f.num));
    f.run_time = (uint16_t*)malloc(sizeof(uint16_t)*(f.num));

	f.func_num[0] = 1;

    run_func();
}


void run_func()
{
  uint8_t i;
  uint8_t j;

  printf("ex)from, to, wait, run_time, r, g, b\n");
  printf("form:0 ~ to:15 wait:500 run_time:0 r:0 g:0 b:0\n");

  f.num = 1;
  f.from[0] = 0;
  f.to[0] = 16;
  f.wait[0] = 500;
  f.run_time[0] = 0;
  f.r[0]=1;
  f.g[0]=1;
  f.b[0]=1;
  

  for(j = 0; j<f.num; j++)
  {
    if(f.func_num[j] == 1)
    {
		printf("---------------11-------");
		  Led(f.from[j],f.to[j],f.wait[j],f.r[j],f.g[j],f.b[j]);
		  delay(f.run_time[j]);
    }
  }
 //Led(0,NUMPIXELS,10,0,0,0);	// LED clear
  printf("Complete!!\n");
}

void PixelColor(uint16_t n, uint32_t rgb)
{
  uint8_t color[3] = {0};
  color[0] = (rgb>>8);
  color[1] = (rgb>>16);
  color[2] = rgb;
  memset(spread_msg+(9*n),0,9);
  byte_index = 0;
  spread_spi_bits(n, color,1);
}
void Led(uint16_t from,uint16_t to,uint16_t wait,uint8_t r,uint8_t g,uint8_t b)
{
  uint16_t i;
  for(i=from; i<=to; i++)
  {
     pixels.setPixelColor(i,pixels.Color(r,g,b));
  }
  pixels.show();
  delay(wait);
}

#define ADV() do { \
      if(bit_mask == 1) \
      {\
         index ++; bit_mask = 0x80; \
      }\
      else \
      {\
         bit_mask >>=1;\
      }\
    } while(0)
void spread_spi_bits(uint8_t start, uint8_t *msg, uint16_t led_num)
{
        uint16_t i,j;
        uint16_t len;
        uint16_t index;
        uint8_t mask,bit_mask;
        
        len = led_num*3; // led * 3. 
        bit_mask = 0x80;
        index = start*9;
        for( i = 0 ; i < len  ; i ++)
        {
                mask = 0x80;
                for( j = 0 ; j < 8 ; j ++, mask >>= 1)
                {
                        if(msg[i] & mask)
                        {
                                spread_msg[index] |= bit_mask ; ADV();
                                spread_msg[index] |= bit_mask ; ADV();
                                ADV();
                        }
                        else
                        {
                                spread_msg[index] |= bit_mask ; ADV();
                                ADV(); ADV();
                        }
                }
        }
        byte_index = index;

  for( i = 0 ; i < byte_index ; i ++)
  {
    //printf("i=%d v = %02x\n",i,spread_msg[i]);
  }
}
