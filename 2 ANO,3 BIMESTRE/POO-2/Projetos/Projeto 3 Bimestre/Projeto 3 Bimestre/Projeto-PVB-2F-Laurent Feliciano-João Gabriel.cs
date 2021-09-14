/*
Colegio Técnico Antônio Teixeira Fernandes (Univap)

Curso Técnico em Informática - Data de Entrega: 14/ 09 / 2021, 14:10

Autores do Projeto: Laurent Chaves Assis Feliciano
                    João Gabriel Pereira da Silva

Turma: 2°F-Informática

Projeto 3° Bimestre de Programação Visual Básica

Observação: Nenhuma

               textBox1 Valor do produto
               textBox2 Numero de parcelas
               textBox3 Mostra as parcelas
               textBox8 dia do pagamento
               textBox9 mês do pagamento
               textBox10 ano do pagamento
               label15 total 
               label16 mostra se a parcela está atrasada
*/

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Projeto_3_Bimestre
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        double ValorDaCompra = 0;
        int NumeroDeParcelas = 0;
        double ValorDasParcelas = 0;
        DateTime DataDaCompra;
        DateTime DataDaParcela;
        double ValorTotal = 0;
        int DiaDoPagamento = 0;
        int MesDoPagamento = 0;
        int AnoDoPagamento = 0; 
        double Juros = 0;
        int C = 1;

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            ValorDaCompra = double.Parse(textBox1.Text);

            if (ValorDaCompra <= 0)
                MessageBox.Show("Não foi possível realizar a conta pois o valor da compra é negativo ou igual a 0");

            NumeroDeParcelas = int.Parse(textBox2.Text);

            if (NumeroDeParcelas <= 0)
                MessageBox.Show("Não foi possível realizar a conta pois o numero de parcelas é negativo ou igual a 0");

            ValorDasParcelas = ValorDaCompra / NumeroDeParcelas;
            Juros = ValorDasParcelas * (3 / 100);
            ValorTotal = ValorDaCompra;

            DataDaCompra = DateTime.Now;
            DateTime DataDaCompra2 = DataDaCompra;

            label15.Text = String.Format("{0:C2}",ValorDaCompra);

            for (int C = 1; C <= NumeroDeParcelas; C++)
            {
                DataDaCompra2 = DataDaCompra2.AddMonths(1);
                DataDaParcela = DataDaCompra;
                if (C == 1)
                    DataDaParcela = DataDaCompra2;
                if (DataDaCompra2.DayOfWeek == DayOfWeek.Sunday){

                    DateTime DataDaCompra3 = DataDaCompra2.AddDays(1);
                    textBox3.AppendText(C.ToString() + "° parcela:" + String.Format("{0:C2}", ValorDasParcelas) + " | Data de vencimento:" + DataDaCompra3.ToString("dd/MM/yyyy") + Environment.NewLine);
                }
                else if(DataDaCompra2.DayOfWeek == DayOfWeek.Saturday)
                {

                    DateTime DataDaCompra3 = DataDaCompra2.AddDays(2);
                    textBox3.AppendText(C.ToString() + "° parcela:" + String.Format("{0:C2}", ValorDasParcelas) + " | Data de vencimento:" + DataDaCompra3.ToString("dd/MM/yyyy") + Environment.NewLine);

                }
                
                else
                {
                    textBox3.AppendText(C.ToString() + "° parcela:" + String.Format("{0:C2}", ValorDasParcelas) + " | Data de vencimento:" + DataDaCompra2.ToString("dd/MM/yyyy") + Environment.NewLine);
                }

            }
            textBox1.Clear();
            textBox2.Clear();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click_1(object sender, EventArgs e)
        {

        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {

        }

        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void label14_Click(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int C2;
            DiaDoPagamento = int.Parse(textBox8.Text);
            MesDoPagamento = int.Parse(textBox9.Text);
            AnoDoPagamento = int.Parse(textBox10.Text);
            DateTime DataDoPagamento = new DateTime(AnoDoPagamento, MesDoPagamento, DiaDoPagamento);
            DataDaParcela = DataDaParcela.AddMonths(1);
            int DiaDaSemana = (int)DataDaParcela.DayOfWeek;
            if (DiaDaSemana == 0)
            {
                MessageBox.Show("Não foi possível realizar o pagamento pois é Domingo");
            }
            else if (DiaDaSemana == 6)
            {
                MessageBox.Show("Não foi possível realizar o pagamento pois é Sábado");
            }
            else if (AnoDoPagamento < DataDaCompra.Year || MesDoPagamento < DataDaCompra.Month && AnoDoPagamento == DataDaCompra.Year || DiaDoPagamento < DataDaCompra.Day && MesDoPagamento == DataDaCompra.Month && AnoDoPagamento == DataDaCompra.Year)
            {
                MessageBox.Show("Não foi possível realizar o pagamento pois a data de pagamento é anterior a data de compra.");
            }
            else
            {
                textBox3.Clear();
                ValorTotal -= ValorDasParcelas;
                label15.Text = String.Format("{0:C2}", ValorTotal);
                if (C <= NumeroDeParcelas)
                {
                    DateTime DataDaCompra2 = DataDaCompra;
                    for(C2=C+1;C2<= NumeroDeParcelas;C2++)
                    {
                        DataDaCompra2 = DataDaCompra2.AddMonths(C2);
                        int dias = (int)DataDaCompra2.DayOfWeek;
                        if (dias == 0)
                        {
                            DateTime DataDaCompra3 = DataDaCompra2.AddDays(1);
                            textBox3.AppendText(C2.ToString() + "° parcela:" + String.Format("{0:C2}", ValorDasParcelas) + " | Data de vencimento:" + DataDaCompra3.ToString("dd/MM/yyyy") + Environment.NewLine);
                        }
                        else if (dias == 6)
                        {
                            DateTime DataDaCompra3 = DataDaCompra2.AddDays(2);
                            textBox3.AppendText(C2.ToString() + "° parcela:" + String.Format("{0:C2}", ValorDasParcelas) + " | Data de vencimento:" + DataDaCompra3.ToString("dd/MM/yyyy") + Environment.NewLine);
                        }
                        else
                        {
                            textBox3.AppendText(C2.ToString() + "° parcela:" + String.Format("{0:C2}", ValorDasParcelas) + " | Data de vencimento:" + DataDaCompra2.ToString("dd/MM/yyyy") + Environment.NewLine);
                        }
                    }
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
