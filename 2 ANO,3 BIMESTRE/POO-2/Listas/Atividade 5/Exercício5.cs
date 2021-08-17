/* *******************************************************************
* Colegio Técnico Antônio Teixeira Fernandes (Univap)
* Curso Técnico em Informática - Data de Entrega: 14/08/2020
* Autores do Projeto: Laurent Chaves Assis Feliciano
* Turma: 2F-Informática
* Atividade 5
* Observação: nenhuma
* Exercício5.cs
* ************************************************************/
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Forms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int Dia = int.Parse(textBox1.Text);
            int Mes = int.Parse(textBox2.Text);
            int Ano = int.Parse(textBox3.Text);
            int N1 = int.Parse(textBox4.Text);
            int N2 = int.Parse(textBox5.Text);
            int N3 = int.Parse(textBox6.Text);
            int N4 = int.Parse(textBox7.Text);
            int N5 = int.Parse(textBox8.Text);
            int N6 = int.Parse(textBox9.Text);
            DateTime Data = new DateTime(Ano,Mes,Dia);
            int Resultado = N1 + N2 + N3 + N4 + N5 + N6;
            int[] Lista = new int[6] {N1,N2,N3,N4,N5,N6};
            int C;
            for (C = 0;C < 6; C++)
            {
                textBox10.AppendText("No Mês  "+data.ToString("MMMM") + ", o Time marcou "+lista[cont]+ Environment.NewLine);
                Data = Data.AddMonths(1);
            }
            textBox10.AppendText("D Time pontuou "+Resultado+" pontos");
        }
    }
}
