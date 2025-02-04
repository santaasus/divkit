package com.yandex.div.core.view2.divs.widgets

import android.content.Context
import android.graphics.Canvas
import android.util.AttributeSet
import com.yandex.div.R
import com.yandex.div.core.Disposable
import com.yandex.div.core.annotations.Mockable
import com.yandex.div.core.expression.ExpressionSubscriber
import com.yandex.div.core.view2.divs.updateBorderDrawer
import com.yandex.div.core.widget.AdaptiveMaxLines
import com.yandex.div.core.widget.invalidateAfter
import com.yandex.div.json.expressions.ExpressionResolver
import com.yandex.div.util.UiThreadHandler
import com.yandex.div.view.SuperLineHeightTextView
import com.yandex.div2.DivBorder
import com.yandex.div2.DivText

@Mockable
internal class DivLineHeightTextView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    private val defStyleAttr: Int = R.attr.divTextStyle
) : SuperLineHeightTextView(context, attrs, defStyleAttr), DivAnimator, DivBorderSupports, TransientView,
    ExpressionSubscriber {

    internal var div: DivText? = null
    internal var adaptiveMaxLines: AdaptiveMaxLines? = null

    internal var animationStartDelay = 0L
    private var animationStarted = false

    private var borderDrawer: DivBorderDrawer? = null
    override val border: DivBorder?
        get() = borderDrawer?.border

    override fun getDivBorderDrawer() = borderDrawer

    override var isTransient = false
        set(value) = invalidateAfter {
            field = value
        }

    override val subscriptions = mutableListOf<Disposable>()

    private var isDrawing = false

    override fun setBorder(border: DivBorder?, resolver: ExpressionResolver) {
        borderDrawer = updateBorderDrawer(border, resolver)
    }

    override fun onSizeChanged(w: Int, h: Int, oldw: Int, oldh: Int) {
        super.onSizeChanged(w, h, oldw, oldh)
        borderDrawer?.onBoundsChanged(w, h)
    }

    override fun draw(canvas: Canvas) {
        isDrawing = true
        borderDrawer.drawClipped(canvas) { super.draw(canvas) }
        isDrawing = false
    }

    override fun dispatchDraw(canvas: Canvas) {
        if (isDrawing) {
            super.dispatchDraw(canvas)
        } else {
            borderDrawer.drawClipped(canvas) { super.dispatchDraw(canvas) }
        }
    }

    override fun startDivAnimation() {
        super.startDivAnimation()
        animationStarted = true
        UiThreadHandler.get().postDelayed({ if (animationStarted) isSelected = true }, animationStartDelay)
    }

    override fun stopDivAnimation() {
        super.stopDivAnimation()
        animationStarted = false
        isSelected = false
    }

    override fun release() {
        super.release()
        borderDrawer?.release()
    }
}
