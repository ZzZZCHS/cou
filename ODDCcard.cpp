#include<bits/stdc++.h>
using namespace std;
int tp,totalnum,playernum,usernum,huihe;
int TP[10][11],KU[31][2][5],hand[10][5],HAND[50][5],L[5],R[5],cardnum[5],cardNum[5];
int suiji[5],ord[5];
string TPname[10],Cardname[21];
struct Player
{
	int health;
	int action;
	int knife;
	int gun;
	int biscuit;
	int drinks;
	bool door;
	bool bus;
	bool dj;
	bool indj;
	int place;
	bool hidden;
	int targeting;
	int Face;
	int face[5];
	int Targeted;
	int targeted[5];
	bool wangzhezhipai;
	bool pilao;
	int pilaoshu;
};
Player player[5];
void preparecard(int x)
{
	int i,flag,r,t,j;
	cout<<"玩家"<<x<<"选取套牌"<<endl;
	for (i=1;i<=tp;i++)
	cout<<i<<"."<<TPname[i]<<" ";
	cout<<endl;
	flag=0;
    while (flag==0)
	{
		cin>>r;
		if ((r>=1)&&(r<=tp))
		{
			flag=1;t=0;
			for (i=1;i<=10;i++)
			for (j=1;j<=TP[r][i];j++)
			{
				t++;KU[t][1][x]=i;
				KU[t][2][x]=rand()%1000;
			}
			for (i=1;i<=29;i++)
			for (j=i+1;j<=30;j++)
			if (KU[i][2][x]>KU[j][2][x])
			{
				r=KU[i][1][x];KU[i][1][x]=KU[j][1][x];KU[j][1][x]=r;
				r=KU[i][2][x];KU[i][2][x]=KU[j][2][x];KU[j][2][x]=r;
			}
//			cout<<"玩家"<<x<<"的牌库是"<<endl;
//			for (i=1;i<=30;i++)
//			cout<<Cardname[KU[i][1][x]]<<" ";
//			cout<<endl;
		}
		else
		{
			cout<<"无效操作"<<endl; 
		}	
	}	 
	return;
}
void fapai(int x)
{
	int i;
	L[x]=1;R[x]=30;
	cardnum[x]=0;cardNum[x]=0;
	cardnum[x]++;hand[cardnum[x]][x]=KU[L[x]][1][x];L[x]++;
	cardnum[x]++;hand[cardnum[x]][x]=KU[L[x]][1][x];L[x]++;
	cardNum[x]++;HAND[cardNum[x]][x]=11;
	cardNum[x]++;HAND[cardNum[x]][x]=12;
//	cout<<"玩家"<<x<<"的套牌手牌为："<<endl;
//	for (i=1;i<=cardnum[x];i++)
//	cout<<Cardname[hand[i][x]]<<" ";
//	cout<<endl;
//	cout<<"玩家"<<x<<"的衍生手牌为："<<endl;
//	for (i=1;i<=cardNum[x];i++)
//	cout<<Cardname[HAND[i][x]]<<" ";
//	cout<<endl; 
	return;
}
void actionjudge(int x)
{
	int i,flag,t;
	flag=0;
	while (flag==0)
	{
		t=0;
		i=1;
		while (i<=totalnum)
		{
			if (player[i].health>0) 
			{
				suiji[i]=rand()%2;
				t=t+suiji[i];
			}
			i++;
		}
		if ((t>0)&&(t<x))
		{
			flag=1;
			for (i=1;i<=totalnum;i++)
			if (player[i].health>0)
			{
			    if (suiji[i]==1)
			    {
				    usernum++;
				    ord[usernum]=i;
				    player[i].action=2*t;
				    if (2*t>6) player[i].action=6;
			    }
			    else {
				    player[i].action=-1;
			    }
		    }
		}
	}
	return;
}
void xirupaiku(int x)
{
	int i,j,r;
	L[x]=1;R[x]=0;
	for (i=1;i<=cardnum[x];i++)
	{
		R[x]++;KU[R[x]][1][x]=hand[i][x];
		KU[R[x]][2][x]=rand()%1000;
	}
	for (i=1;i<=R[x]-1;i++)
	for (j=i+1;j<=R[x];j++)
	if (KU[i][2][x]>KU[j][2][x])
	{
		r=KU[i][1][x];KU[i][1][x]=KU[j][1][x];KU[j][1][x]=r;
		r=KU[i][2][x];KU[i][2][x]=KU[j][2][x];KU[j][2][x]=r;
	}
	return;
}
void drawcards(int x)
{
	int i,j;
	i=1;
	while (i<=totalnum)
	{
		if (player[i].health>0)
		{
			if (player[i].action>0)
			{
				for (j=1;j<=2;j++)
				{
					if (L[i]<=R[i])
					{
                        cardnum[i]++;hand[cardnum[i]][i]=KU[L[i]][1][i];L[i]++;
                    }
                    else if (player[i].wangzhezhipai==false)
                    {
                    	xirupaiku(i);
                    	player[i].wangzhezhipai=true;
                    	cardnum[i]++;hand[cardnum[i]][i]=KU[L[i]][1][i];L[i]++;
					}
					else 
					{
						player[i].pilao=true;
					}
			    }
			    if (player[i].pilao==true)
			    player[i].pilaoshu++; 
			}
			else
			{
				if (L[i]<=R[i])
				{
                    cardnum[i]++;hand[cardnum[i]][i]=KU[L[i]][1][i];L[i]++;
                }
                else if (player[i].wangzhezhipai==false)
                {
                    xirupaiku(i);
                    player[i].wangzhezhipai=true;
                    cardnum[i]++;hand[cardnum[i]][i]=KU[L[i]][1][i];L[i]++;
				}
				else 
				{
					player[i].pilao=true;
					player[i].pilaoshu++; 
				}
			}
		}
		i++;
	}
	return;
}
int main()
{
	int i,rpl,flaG1;
	tp=2;
	Cardname[1]="shopping";Cardname[2]="buyweapon";Cardname[3]="buyfood";Cardname[4]="goforsomeone";Cardname[5]="search";
	Cardname[6]="estfood";Cardname[7]="hitting";Cardname[8]="shooting";Cardname[9]="hidding";Cardname[10]="dijiao";
	Cardname[11]="opendoor";Cardname[12]="drivecar";Cardname[13]="luckypenny";Cardname[14]="aimat";
	TPname[1]="quick attack";TPname[2]="healing is great";
	TP[1][1]=4;TP[1][2]=4;TP[1][3]=0;TP[1][4]=7;TP[1][5]=0;TP[1][6]=0;TP[1][7]=15;TP[1][8]=0;TP[1][9]=0;TP[1][10]=0;
	srand((int)time(NULL));
	cout<<"ODDC-都市之弈"<<endl;
	cout<<1<<".开始游戏"<<" "<<2<<".编辑套牌"<<" "<<3<<".退出游戏"<<endl;
	flaG1=0;
	while (flaG1==0)
	{
		cin>>rpl;
	    if (rpl==1)
	    {
	    	flaG1=1;
	    	cout<<"玩家人数2~4"<<endl;
			flaG1=0;
			while (flaG1==0)
			{
				cin>>rpl;
				if ((rpl<=4)&&(rpl>=2))
				{
					flaG1=1;
					playernum=rpl;
					totalnum=rpl;
				}
				else
				{
					cout<<"无效操作"<<endl;
				}
			} 
	    	for (i=1;i<=playernum;i++)
	    	preparecard(i);
	    	for (i=1;i<=playernum;i++)
	    	fapai(i);
	    	flaG1=0;
	    	for (i=1;i<=playernum;i++)
	    	player[i].health=4;
	    	huihe=0;
	    	while (flaG1==0)
	    	{
	    		huihe++;
	    		cout<<"第"<<huihe<<"回合"<<endl; 
	    		usernum=0;
	    		actionjudge(playernum);
	    		drawcards(playernum);
	    		cout<<"玩家"<<1<<"的套牌手牌为："<<endl;
             	for (i=1;i<=cardnum[1];i++)
            	cout<<Cardname[hand[i][1]]<<" ";
            	cout<<endl;
            	cout<<"玩家"<<2<<"的衍生手牌为："<<endl;
            	for (i=1;i<=cardNum[2];i++)
	            cout<<Cardname[HAND[i][2]]<<" ";
            	cout<<endl;
	    		break;
//	    		decideorder(usernum);
//	    		for (i=1;i<=usernum;i++)
//	    		usecards(ord[i]);
//	    		if (playernum<2) flaG1=1;
//	    		for (i=1;i<=playernum;i++)
//	    		abandoncards(i);
//	    		if (playernum<2) flaG1=1;
			}
	    }
	    else if (rpl==2)
	    {
	    	flaG1=1;
  	    }
  	    else if (rpl==3)
  	    {
  	    	flaG1=1;
		}
	    else
	    {
	    	cout<<"无效操作"<<endl;
	    }
    }
	return 0; 
} 
