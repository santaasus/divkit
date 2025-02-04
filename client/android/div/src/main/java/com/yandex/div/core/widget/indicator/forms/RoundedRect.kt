package com.yandex.div.core.widget.indicator.forms

import android.graphics.Canvas
import android.graphics.Paint
import android.graphics.RectF
import com.yandex.div.core.widget.indicator.IndicatorParams

class RoundedRect(private val params: IndicatorParams.Style) : SingleIndicatorDrawer {

    private val paint = Paint()
    private val shape = params.shape as IndicatorParams.Shape.RoundedRect
    private val rect = RectF(0f, 0f, shape.normalWidth, shape.normalHeight)

    override fun draw(canvas: Canvas, x: Float, y: Float, itemSize: IndicatorParams.ItemSize, color: Int) {
        val rectSize = itemSize as IndicatorParams.ItemSize.RoundedRect
        paint.color = color
        rect.apply {
            left = x - rectSize.itemWidth / 2f
            top = y - rectSize.itemHeight / 2f
            right = x + rectSize.itemWidth / 2f
            bottom = y + rectSize.itemHeight / 2f
        }
        canvas.drawRoundRect(rect, rectSize.cornerRadius, rectSize.cornerRadius, paint)
    }

    override fun drawSelected(canvas: Canvas, rect: RectF) {
        val rectSize = params.shape.normalItemSize as IndicatorParams.ItemSize.RoundedRect
        paint.color = params.selectedColor

        canvas.drawRoundRect(rect, rectSize.cornerRadius, rectSize.cornerRadius, paint)
    }
}
